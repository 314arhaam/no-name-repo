import sys, argparse, os
import sqlalchemy
import pandas as pd
from . import db

class MySQL(db.DB):
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

    def insert_df(self, dest_table: str, data: pd.DataFrame):
        if len(dest_table.split('.')) != 2:
            raise ValueError("`dest_table` must be [SCHEMA].[TABLE NAME] format.")
        else:
            schema, table = dest_table.split(".")
        with self.client.begin() as conn:
            data.to_sql(
                name=table,
                schema=schema,
                con=conn,
                if_exists="append",
                index=False,
                method="multi"
            )


if __name__ == '__main__':
    ms = MySQL()
    print(ms.ping())
