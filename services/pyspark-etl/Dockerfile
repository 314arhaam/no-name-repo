FROM bitnamilegacy/spark:3.5

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt 

ENTRYPOINT ["spark-submit"]