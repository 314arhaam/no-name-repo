FROM python:3.12-slim

WORKDIR ./reporter_app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "reporter_app/main.py"]