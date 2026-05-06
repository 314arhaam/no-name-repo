from faker import Faker
import faker_commerce
import pandas as pd
import random

def generate(n: int) -> pd.DataFrame:
    fake = Faker()
    fake.add_provider(faker_commerce.Provider)
    data = {
        "product_id": [],
        "product_name": [],
        "price": []
    }
    product_id_set = set()
    for i in range(n):
        while True:
            product_id = int("100" + str(random.randint(1, 10000*n)))
            if product_id not in product_id_set:
                product_id_set.add(product_id)
                break
        data["product_id"].append(product_id)
        data["product_name"].append(fake.unique.ecommerce_name())
        data["price"].append(random.randint(1, 100))
    return pd.DataFrame(data)