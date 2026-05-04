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
    user_id_set = set()
    for i in range(n):
        while True:
            user_id = int("100" + str(random.randint(1, 10000*n)))
            if user_id not in user_id_set:
                user_id_set.add(user_id)
                break
        data["user_id"].append(user_id)
        name = fake.name()
        data["first_name"].append(name.split()[0])
        data["last_name"].append(name.split()[1])
        data["city"].append(fake.city())
        data["address"].append(fake.street_address())
        data["email"].append(fake.unique.safe_email())
        data["is_pro"] = (random.randint(1, 100) % 5 == 0)
    return pd.DataFrame(data)