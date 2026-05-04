import pandas as pd
import clickhouse_driver
import os, dotenv, uuid, random, datetime

class BannerView:
    def __init__(self, n_banners: int = 10, n_users: int = 100):
        self.n_banners = n_banners
        self.n_users = n_users
    def generate(self, n: int) -> pd.DataFrame:
        data_list = []
        for i in range(n):
            data = {
                "event_time": datetime.datetime.now().strftime("%Y-%m%d %H:%M:%S"),
                "banner_id": random.randint(1, self.n_banners+1),
                "user_id": random.randint(1, self.n_users+1)
            }
            data_list.append(data)
        return pd.DataFrame(data_list)

if __name__ == "__main__":
    dataset = BannerView().generate(10)
    print(dataset)