import pandas as pd
import clickhouse_driver
import os, random, datetime, sys

class BannerView:
    def __init__(self, n_banners: int = 10, n_users: int = 100):
        self.n_banners = n_banners
        self.n_users = n_users
    def generate(self, n: int) -> pd.DataFrame:
        data_list = []
        for i in range(n):
            data = {
                "event_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "banner_id": random.randint(1, self.n_banners+1),
                "user_id": random.randint(1, self.n_users+1)
            }
            data_list.append(data)
        return pd.DataFrame(data_list)

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except IndexError:
        n = 100
    data = BannerView().generate(n)
    print(data)
    client = clickhouse_driver.Client(
        host = os.getenv("CLICKHOUSE_HOST"),
        port = os.getenv("CLICKHOUSE_PORT"),
        user = os.getenv("CLICKHOUSE_USER"),
        password = os.getenv("CLICKHOUSE_PASSWORD"),
    )
    client.insert_dataframe(
        "cicd_test_event_db.banner_view",
        data
    )