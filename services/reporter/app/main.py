import src.mysql
import src.clickhouse
import sys, json, argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Query to Dataframe CLI")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--config', type=str, help='Config string')
    group.add_argument('--file', type=str, help='Config file path')
    args = parser.parse_args()
    if args.config:
        config = json.loads(args.config)
    elif args.file:
        with open(args.file, 'r') as f:
            config = json.load(f)
    else:
        raise ValueError("Specify --config or --file")
    if "driver" not in config.keys() or "query" not in config.keys():
        raise KeyError("Config file requires `driver` and `query` fields.")
    match config["driver"]:
        case "clickhouse":
            driver = src.clickhouse.ClickHouse()
        case "mysql":
            driver = src.mysql.MySQL()
    data = driver.query_df(config["query"])
    if config.get("output"):
        data.to_csv(config["output"])
    else:
        print(data.head())