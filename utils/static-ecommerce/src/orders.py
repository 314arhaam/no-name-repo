from faker import Faker
import faker_commerce
import pandas as pd
import random

def generate(n: int, num_user: int, num_product: int) -> pd.DataFrame:
    fake = Faker()
    data = {
        "order_id": [],
        "create_at": [],
        "user_id": [],
        "product_id": [],
        "order_status": []
    }
    product_id_set = set()
    for i in range(n):
        data["order_id"].append(i)
        data["create_at"].append(fake.date_time_this_month())
        p_list = []
        for j in range(random.randint(1, 5)):
            p_list.append(random.randint(0, num_product-1))
        data["product_id"].append(p_list)
        data["user_id"].append(random.randint(0, num_user-1))
        data["order_status"].append(["SUCCESS", "FAILED"][int(random.randint(0, 100)%4 == 0)])
    df = pd.DataFrame(data)
    df = df.explode(column = ["product_id"]).reset_index(drop = True)
    df = df.reset_index().rename(columns = {"index": "id_"})
    return df