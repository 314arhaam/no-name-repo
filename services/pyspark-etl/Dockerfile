FROM bitnamilegacy/spark:3.5

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt 
RUN mkdir jar/ 
RUN curl -L -o jar/mysql.jar https://maven.org 
RUN curl -L -o jar/clickhouse.jar https://maven.org

ENTRYPOINT ["spark-submit"]