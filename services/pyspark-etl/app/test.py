from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .appName("Test_Job") \
    .getOrCreate()

print("HELLO")

spark.stop()