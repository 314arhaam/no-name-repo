FROM python:3.12-slim

WORKDIR ./reporter

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "app/main.py"]