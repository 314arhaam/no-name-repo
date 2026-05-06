FROM python:3.12-slim

WORKDIR ./etl

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && mkdir app/src

COPY ../reporter/app/src/db.py ../reporter/app/src/mysql.py ../reporter/app/src/clickhouse.py app/src

CMD ["python3", "app/main.py"]