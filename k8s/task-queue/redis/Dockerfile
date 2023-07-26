FROM python:3.10-slim

WORKDIR /app
ENV PORT=8080

RUN apt-get update && apt-get install -y gcc python3-dev

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

CMD gunicorn --workers 10 --bind 0.0.0.0:8080 --log-level DEBUG main:app

