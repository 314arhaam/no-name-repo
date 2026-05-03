from clickhouse_driver import Client

client = Client(
    host="localhost",
    port=9000,
    user="test_user",
    password="test_password"
)

result = client.execute("SELECT version()")
print(result)
