import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import (StructType, StructField, StringType, IntegerType,
                               DoubleType, DateType)
from pyspark.errors import PySparkException

import src.logger as log
from src.utils import add_timestamp

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

    def create_dataframe(self, csv_file: str) -> pyspark.sql.DataFrame:
        """
        Create a dataframe from a provided CSV file.
        :param csv_file: a CSV file from which to create a data frame.
        :return: returns a data frame created from the provided CSV file.
        """
        try:
            if not csv_file:
                staging_logger.info('CSV file was not provided')

            dataframe = self.spark.read.csv(csv_file, header=True)

        except PySparkException as err:
            staging_logger.info('A PySpark exception occurred while creating a data frame: %s', err, exc_info=True)

        return dataframe

    def apply_schema(self,
                     dataframe: pyspark.sql.DataFrame,
                     schema_name: str) -> pyspark.sql.DataFrame:
        """

        :param dataframe:
        :param schema_name:
        :return:
        """

        return dataframe

    def upload_to_db(self, dataframe: pyspark.sql.DataFrame):
        """

        :param dataframe:
        :return:
        """
