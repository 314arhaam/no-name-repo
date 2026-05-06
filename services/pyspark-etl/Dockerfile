FROM bitnamilegacy/spark:3.5

WORKDIR ./app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt \
    mkdir jar/ \
    curl -L -o jar/mysql.jar https://maven.org
    curl -L -o jar/clickhouse.jar https://maven.org

ENTRYPOINT ["spark-submit"]