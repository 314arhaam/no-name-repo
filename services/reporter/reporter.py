from clickhouse_connect
import dotenv, os

if __name__ == '__main__':
    # load env file
    dotenv.load_dotenv()
    # create clickhouse client
    client = clickhouse_connect.get_client(
        host="localhost",
        port=8123,
        username=os.getenv("CLICKHOUSE_USER"),
        password=os.getenv("CLICKHOUSE_PASSWORD")
    )
    # fetch version
    result = client.query_df("SELECT * FROM cicd_test_event_db.banner_view limit 10")
    print(result)
