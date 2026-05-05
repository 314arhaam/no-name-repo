import sys, argparse, os
import sqlalchemy
import pandas as pd
import clickhouse_connect

def create_mysql_engine():
    host = os.getenv("MYSQL_HOST", "localhost")
    port = os.getenv("MYSQL_PORT", "3306")
    database = os.getenv("MYSQL_DATABASE")
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    # SQLAlchemy engine string for MySQL (PyMySQL driver)
    engine = sqlalchemy.create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4",
        echo=False,
        pool_recycle=3600
    )
    return engine

if __name__ == "__main__":
    mysql_engine = create_mysql_engine()
    extract_data = pd.read_sql(
        f"""SELECT DATE(create_at) as date_, count(distinct order_id) as order_count 
            FROM fact.order 
            GROUP BY DATE(create_at)
            ORDER BY DATE(create_at)""", 
        con=mysql_engine
    )
    print(extract_data)
    #
    client = clickhouse_connect.get_client(
        host=os.getenv("CLICKHOUSE_HOST"),
        port=os.getenv("CLICKHOUSE_PORT"),
        username=os.getenv("CLICKHOUSE_USER"),
        password=os.getenv("CLICKHOUSE_PASSWORD")
    )
    client.insert_df(
        "analytics.daily_order",
        extract_data
    )
    verify_df = client.query_df("select * from analytics.daily_order")
    print(verify_df)