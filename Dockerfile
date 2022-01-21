FROM python:3.9-slim-buster

WORKDIR /app

ARG type

ENV TYPE=$type

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD sh ./$TYPE.sh