import os
import src.mysql
import src.clickhouse
import pandas as pd

if __name__ == "__main__":
    # extract section
    query = """
        SELECT DATE(create_at) as date_, count(distinct order_id) as order_count 
        FROM fact.order 
        WHERE
            order_status = 'SUCCESS'
        GROUP BY DATE(create_at)
        ORDER BY DATE(create_at)
    """
    mysql = src.mysql.MySQL()
    extract_data = mysql.query_df(query)
    # transform section 
    # load section
    dest_table = "analytics.daily_order"
    ch = src.clickhouse.ClickHouse()
    ch.insert_df(
        "analytics.daily_order",
        extract_data
    )