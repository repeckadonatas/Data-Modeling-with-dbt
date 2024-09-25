from pyspark.sql import SparkSession
from pyspark.sql.types import (StructType, StructField, StringType, IntegerType,
                               DoubleType, DateType)
from pyspark.errors import PySparkException

import src.logger as log
from src.utils import add_timestamp

staging_logger = log.app_logger(__name__)


class DataStaging:

    def __init__(self):
        try:
            self.spark = SparkSession.builder \
                .appName('Sales Data Modelling') \
                .getOrCreate()

        except PySparkException as err:
            staging_logger.info('A PySpark exception occurred: %s', err, exc_info=True)


