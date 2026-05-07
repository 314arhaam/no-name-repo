from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os

spark = SparkSession.builder \
    .appName("MySQL_to_ClickHouse_ETL") \
    .getOrCreate()

source_db = "fact"
source_table = "order"

mysql_df = spark.read \
    .format("jdbc") \
    .option("url", f"jdbc:mysql://{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{source_db}") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", f"{source_db}.{source_table}") \
    .option("user", f"{os.getenv('MYSQL_USER')}") \
    .option("password", f"{os.getenv('MYSQL_PASSWORD')}") \
    .load()

print("[*] Loaded from MySQL:")
mysql_df.printSchema()
mysql_df.show(5)

transformed_df = mysql_df \
    .withColumn("date_", F.to_date("create_at")) \
    .groupBy("date_") \
    .agg(F.countDistinct("order_id").alias("order_count")) \
    .select("date_", "order_count")

print("[*] Transform Done:")
transformed_df.printSchema()
transformed_df.show(5)

sink_db = "analytics"
sink_table = "daily_order"

transformed_df.write \
    .format("jdbc") \
    .mode("append") \
    .option("url", f"jdbc:ch://{os.getenv('CLICKHOUSE_HOST')}:{os.getenv('CLICKHOUSE_PORT')}/{sink_db}") \
    .option("driver", "com.clickhouse.jdbc.ClickHouseDriver") \
    .option("dbtable", f"{sink_db}.{sink_table}") \
    .option("user", f"{os.getenv('CLICKHOUSE_USER')}") \
    .option("password", f"{os.getenv('CLICKHOUSE_PASSWORD')}") \
    .option("batchsize", 100000) \
    .save()

print("[*] Data written to ClickHouse successfully")

spark.stop()
