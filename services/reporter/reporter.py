from clickhouse_driver import Client
import dotenv, os

if __name__ == '__main__':
    # load env file
    dotenv.load_dotenv()
    # create clickhouse client
    client = Client(
        host="localhost",
        port=9000,
        user=os.getenv("CLICKHOUSE_USER"),
        password=os.getenv("CLICKHOUSE_PASSWORD")
    )
    # fetch version
    result = client.execute("SELECT * FROM cicd_test_event_db.banner_view limit 10")
    print(result)
