from faker import Faker
import pandas as pd
import random

def generate(n: int) -> pd.DataFrame:
    fake = Faker()
    data = {
        "user_id": [],
        "first_name": [],
        "last_name": [],
        "city": [],
        "address": [],
        "is_pro": [],
        "email": []
    }
    for i in range(n):
        data["user_id"].append(int("100" + str(random.randint(1, 10000))))
        name = fake.name()
        data["first_name"].append(name.split()[0])
        data["last_name"].append(name.split()[1])
        data["city"].append(fake.city())
        data["address"].append(fake.street_address())
        data["email"].append(fake.safe_email())
        data["is_pro"] = (random.randint(1, 100) % 5 == 0)
    return pd.DataFrame(data)