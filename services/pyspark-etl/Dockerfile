FROM bitnamilegacy/spark:3.5

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt 
RUN mkdir jar/ 
RUN curl -L -o jar/mysql.jar https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.33/mysql-connector-java-8.0.33.jar
RUN curl -L -o jar/clickhouse.jar https://maven.org

ENTRYPOINT ["spark-submit"]