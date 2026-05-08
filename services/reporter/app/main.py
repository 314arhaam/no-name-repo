import src.mysql
import src.clickhouse
import sys, json, argparse, os

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
    if "driver" not in config.keys():
        raise KeyError("Config file requires `driver` field.")
    match config["driver"]:
        case "clickhouse":
            driver = src.clickhouse.ClickHouse()
        case "mysql":
            driver = src.mysql.MySQL()
    if config.get("query"):
        data = driver.query_df(config["query"])
    else:
        for i in range(20):
            try:
                data = driver.ping()
            except Exception as e:
                print(f"Error in ping {e} - retry {i+1} of 20")
                time.sleep(3)
        print(data)
        sys.exit()
    if config.get("output"):
        data.to_csv(config["output"])
    else:
        print(data.head())