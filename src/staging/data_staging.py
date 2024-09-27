from datetime import datetime
from pathlib import Path

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.errors import PySparkException

import src.logger as log
from src.utils import read_dict, get_files_in_directory
from src.constants import FILE_SCHEMA_DICT, PATH_TO_DATA_STORAGE

staging_logger = log.app_logger(__name__)


class SparkSessionManager:

    def __init__(self):
        """
        Starts a Spark Session.
        """
        try:
            self.spark = SparkSession.builder \
                .appName('Sales Data Modelling') \
                .getOrCreate()
            staging_logger.info('Spark Session for "Sales Data Modelling" started')

        except PySparkException as err:
            staging_logger.info('A PySpark exception occurred: %s', err, exc_info=True)
            raise

    def __enter__(self):
        """
        For context manager support.
        """
        return self.spark

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes a Spark Session.
        :param exc_type: exception type
        :param exc_val: exception value
        :param exc_tb: exception traceback
        """
        try:
            if self.spark is not None:
                self.spark.stop()
                staging_logger.info('Spark Session closed.')

        except (PySparkException, exc_type, exc_val, exc_tb) as err:
            staging_logger.info('Error closing Spark Session: %s', err, exc_info=True)


def schema_select(csv_file: str) -> (str | None):
    """
    Selects a correct schema based on the CSV file's name.
    :return: schema
    """
    file_schema_select = read_dict(FILE_SCHEMA_DICT)

    for file, (schema_name, schema) in file_schema_select:
        if file == csv_file:
            staging_logger.info('Schema "%s" selected for CSV file "%s"', schema_name, file)
            return schema

        else:
            staging_logger.warning('No schema selected for CSV file "%s"', file)
    return None

def create_dataframe(spark: SparkSession,
                     csv_file: str,
                     schema_name: pyspark.sql.types.StructType) -> pyspark.sql.DataFrame:
    """
    Create a data frame from a provided CSV file.
    Applies a correct schema to the data frame.
    :param spark: Spark Session
    :param csv_file: a CSV file from which to create a data frame.
    :param schema_name: the name of the schema to apply to the data frame.
    :return: returns a data frame created from the provided CSV file with schema applied..
    """
    try:
        if not csv_file:
            staging_logger.warning('CSV file was not provided.')
            raise ValueError('CSV name is required.')

        full_path = Path(PATH_TO_DATA_STORAGE) / csv_file
        if not full_path.exists():
            staging_logger.warning('CSV file does not exist: %s', full_path, exc_info=True)
            raise FileNotFoundError('CSV file not found: %s', full_path)

        dataframe = spark.read \
            .format('csv') \
            .option('header', True) \
            .schema(schema_name) \
            .load(str(full_path))

        return dataframe

    except PySparkException as err:
        staging_logger.info('A PySpark exception occurred while creating a data frame: %s', err, exc_info=True)

def add_timestamp(dataframe: pyspark.sql.DataFrame) -> pyspark.sql.DataFrame:
    """
    Adds a timestamp to the dataframe.
    :param dataframe: a dataframe to add the timestamp to.
    :return: a dataframe with the timestamp added.
    """
    date_now = datetime.now()
    dataframe = dataframe.withColumn('timestamp', lit(date_now))

    return dataframe

def upload_to_db(dataframe: pyspark.sql.DataFrame): #TODO
    """

    :param dataframe:
    :return:
    """

if __name__ == '__main__':
    with SparkSessionManager() as spark:

        csv_files = get_files_in_directory(PATH_TO_DATA_STORAGE)
        for csv_file in csv_files:
            schema_name = schema_select(csv_file)
            if schema_name:
                df = create_dataframe(spark, csv_file, schema_name)
                df = add_timestamp(df)
                df.show(5)
                #TODO
                # upload_to_db(df)
            else:
                staging_logger.warning('Skipping file "%s" processing due to missing schema', csv_file)