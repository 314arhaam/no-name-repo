import clickhouse_connect
import os
import pandas as pd
from . import db

class ClickHouse(db.DB):
    def __init__(self):
        super().__init__()
        client = clickhouse_connect.get_client(
            host=os.getenv("CLICKHOUSE_HOST", "localhost"),
            port=os.getenv("CLICKHOUSE_PORT", "8123"),
            username=os.getenv("CLICKHOUSE_USER"),
            password=os.getenv("CLICKHOUSE_PASSWORD")
        )
        self.client = client
    
    def query_df(self, query: str = "SELECT 1 as test_col") -> pd.DataFrame:
        return self.client.query_df(query)
    
    def ping(self):
        return all(self.query_df() == pd.DataFrame({"test_col": 1}))

if __name__ == '__main__':
    ch = ClickHouse()
    print(ch.ping())
