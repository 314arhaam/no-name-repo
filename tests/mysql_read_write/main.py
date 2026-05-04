import pandas as pd
from sqlalchemy import create_engine
import dotenv, datetime

def main():
    # ---- Connection settings (adjust to your environment) ----
    host = os.getenv("MYSQL_HOST")
    port = os.getenv("MYSQL_PORT")
    database = os.getenv("MYSQL_DATABASE")
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    # SQLAlchemy engine string for MySQL (PyMySQL driver)
    engine = create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4",
        echo=False,  # set to True to debug SQL
        pool_recycle=3600
    )
    # ---- Example DataFrame to write ----
    df_to_write = pd.DataFrame({
        "event_time": [datetime.datetime.now()],
        "banner_id": [1000],
        "user_id": [101],
    })
    table_name = "cicd_test_event_db.banner_view"
    # ---- Write DataFrame to MySQL ----
    # Uses a transaction and replaces table if it already exists
    with engine.begin() as conn:
        df_to_write.to_sql(
            name=table_name,
            con=conn,
            if_exists="replace",
            index=False,
            method="multi"
        )
    # ---- Read data back into a DataFrame with proper column names ----
    df_read = pd.read_sql(f"SELECT * FROM {table_name}", con=engine)
    print("Data written to MySQL:")
    print(df_to_write)
    print("\nData read back from MySQL:")
    print(df_read)
    # Optional: show column names to verify they are preserved
    print("\nRead columns:", list(df_read.columns))

if __name__ == "__main__":
    dotenv.load_dotenv()
    main()
