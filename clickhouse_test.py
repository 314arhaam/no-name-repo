from clickhouse_driver import Client

client = Client(
    host="localhost",
    port=9000,
    username="default",
    password=""
)

result = client.execute("SELECT version()")
print(result)
