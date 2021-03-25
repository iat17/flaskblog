FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add build-base postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip setuptools wheel
RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
ENV FLASK_ENV='development'

EXPOSE 8000

ENTRYPOINT ["python", "server.py"]
