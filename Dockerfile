FROM python:3.13.3

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]
