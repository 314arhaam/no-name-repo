import sys, argparse, os
import sqlalchemy
import pandas as pd
from db import DB

class MySQL(DB):
    def __init__(self):
        super().__init__()
        host = os.getenv("MYSQL_HOST", "localhost")
        port = os.getenv("MYSQL_PORT", "3306")
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        # SQLAlchemy engine string for MySQL (PyMySQL driver)
        engine = sqlalchemy.create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}?charset=utf8mb4",
            echo=False,
            pool_recycle=3600
        )
        self.client = engine
    
    def query_df(self, query: str = "SELECT 1 as test_col") -> pd.DataFrame:
        return pd.read_sql(
            query, 
            con=self.client
        )
    
    def ping(self):
        return all(self.query_df() == pd.DataFrame({"test_col": [1]}))

if __name__ == '__main__':
    ms = MySQL()
    print(ms.ping())
