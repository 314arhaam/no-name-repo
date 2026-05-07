FROM bitnamilegacy/spark:3.5

WORKDIR /pyspark-etl-job

COPY . .

RUN pip install --no-cache-dir -r requirements.txt 

# ENTRYPOINT ["spark-submit"]