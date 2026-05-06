FROM bitnamilegacy/spark:3.5

WORKDIR ./app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt \
    mkdir jar/ \
<<<<<<< HEAD
    curl -L -o jar/mysql.jar https://maven.org
=======
    curl -L -o jar/mysql.jar https://maven.org \
>>>>>>> 26f48d4 (better dep manage (jar))
    curl -L -o jar/clickhouse.jar https://maven.org

ENTRYPOINT ["spark-submit"]