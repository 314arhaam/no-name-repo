import src.users
import src.products
import src.orders
import sys, argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u", 
        "--user",
        default=100,
        type=int
    )
    parser.add_argument(
        "-p", 
        "--product",
        default=100,
        type=int
    )
    parser.add_argument(
        "-o", 
        "--order",
        default=1000,
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
    if not args.sql:
        print(users_df)
        print(products_df)
        print(orders_df)
    else:
        print("Not implemented")