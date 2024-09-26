import pyspark
from pyspark.sql import SparkSession
from pyspark.errors import PySparkException

import src.logger as log
from src.utils import read_dict, add_timestamp
from src.constants import FILE_SCHEMA_DICT

staging_logger = log.app_logger(__name__)


class DataStaging:  #TODO

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

    def __exit__(self, exc_type, exc_val, exc_tb):  #TODO
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
            staging_logger.info('Spark Session was not closed:: %s', err, exc_info=True)

    def schema_select(self, csv_file: str) -> str:
        """
        Selects a correct schema based on the CSV file's name.
        :return:
        """
        file_schema_select = read_dict(FILE_SCHEMA_DICT)

        for file, schema in file_schema_select:
            if file == csv_file:
                schema_name = schema
                staging_logger.info('Schema "%s" selected for CSV file "%s"', schema, file)
            else:
                staging_logger.info('No schema selected for CSV file "%s"', file)

        return schema_name

    def create_dataframe(self,
                         csv_file: str,
                         schema_name: str) -> pyspark.sql.DataFrame:
        """
        Create a data frame from a provided CSV file.
        Applies a correct schema to the data frame.
        :param csv_file: a CSV file from which to create a data frame.
        :param schema_name: the name of the schema to apply to the data frame.
        :return: returns a data frame created from the provided CSV file with schema applied..
        """
        try:
            if not csv_file:
                staging_logger.info('CSV file was not provided')

            dataframe = self.spark.read \
                .format('csv') \
                .schema(schema_name) \
                .option('header', True) \
                .load(csv_file)


        except PySparkException as err:
            staging_logger.info('A PySpark exception occurred while creating a data frame: %s', err, exc_info=True)

        return dataframe

    def upload_to_db(self, dataframe: pyspark.sql.DataFrame):
        """

        :param dataframe:
        :return:
        """
