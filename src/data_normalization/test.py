import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

print(pyspark.__version__)

spark = SparkSession.builder \
    .appName("Sales Data Modeling") \
    .getOrCreate()

data_path = "../input/circuits.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)
df.printSchema()
