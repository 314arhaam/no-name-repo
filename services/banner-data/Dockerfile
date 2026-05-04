FROM python3.12-slim

WORKDIR app/

COPY . .

RUN pip install -i https://package-mirror.liara.ir/repository/pypi/simple --no-cache-dir -r requirements.txt

CMD ["python3", "app/main.py"]