FROM python:3.12-slim

WORKDIR banner_data_generator

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "banner_data_generator/app/main.py"]