import src.users
import src.products
import src.orders
import sys, argparse, os
import sqlalchemy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u", 
        "--user",
        default=2,
        type=int
    )
    parser.add_argument(
        "-p", 
        "--product",
        default=2,
        type=int
    )
    parser.add_argument(
        "-o", 
        "--order",
        default=10,
        type=int
    )
    parser.add_argument(
        "-s", 
        "--sql",
        action="store_true"
    )
    args = parser.parse_args()
    users_df = src.users.generate(args.user)
    products_df = src.products.generate(args.product)
    orders_df = src.orders.generate(args.order, args.user, args.product)
    orders_df = orders_df.merge(
        products_df.reset_index()[["index", "product_id"]],
        how='left',
        suffixes = ("_",""),
        right_on = "index",
        left_on = "product_id"
    ).drop(
        columns = ["index", "product_id_"]
    ).merge(
        users_df.reset_index()[["index", "user_id"]],
        how='left',
        suffixes = ("_",""),
        right_on = "index",
        left_on = "user_id"
    ).drop(
        columns = ["index", "user_id_"]
    )
    if args.sql:
        print(users_df)
        print(products_df)
        print(orders_df)
    else:
        host = os.getenv("MYSQL_HOST", "localhost")
        port = os.getenv("MYSQL_PORT", "3306")
        database = os.getenv("MYSQL_DATABASE")
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        # SQLAlchemy engine string for MySQL (PyMySQL driver)
        engine = sqlalchemy.create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4",
            echo=False,  # set to True to debug SQL
            pool_recycle=3600
        )
        db = 'cicd_test_event_db'
        table_name = "banner_view"
        config = [
            ("dim", "user", users_df),
            ("dim", "product", products_df),
            ("fact", "order", orders_df)
        ]
        # ---- Write DataFrame to MySQL ----
        for conf in config:
            with engine.begin() as conn:
                conf[2].to_sql(
                    name=conf[1],
                    schema=conf[0],
                    con=conn,
                    if_exists="append",
                    index=False,
                    method="multi"
                )
        # ---- Read data back into a DataFrame with proper column names ----
        df_read = pd.read_sql(f"SELECT * FROM fact.order", con=engine)
        print(df_read)