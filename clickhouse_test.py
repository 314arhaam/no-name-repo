import clickhouse_connect

client = clickhouse_connect.get_client(
    host="localhost",
    port=9000,
    username="default",
    password=""
)

result = client.query("SELECT version()")
print(result.result_rows[0][0])
