import clickhouse_connect
import os

if __name__ == '__main__':
    # create clickhouse client
    client = clickhouse_connect.get_client(
        host=os.getenv("CLICKHOUSE_HOST"),
        port=os.getenv("CLICKHOUSE_PORT"),
        username=os.getenv("CLICKHOUSE_USER"),
        password=os.getenv("CLICKHOUSE_PASSWORD")
    )
    # fetch version
    result = client.query_df("SELECT * FROM cicd_test_event_db.banner_view limit 10")
    print(result)
