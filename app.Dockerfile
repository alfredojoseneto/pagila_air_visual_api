FROM python:3.12-slim-bookworm

WORKDIR /workdir

COPY app app

RUN apt update && \
    apt install -y \
        build-essential \
        libpq-dev \
        python3-dev && \
    pip install -r ./app/requirements.txt

ARG POSTGRES_USER
ARG POSTGRES_PASSWORD
ARG POSTGRES_HOST
ARG POSTGRES_PORT
ARG POSTGRES_DATABASE
ARG AIRVISUAL_KEY 
ARG WEATHER_KEY

ENV AIRVISUAL_KEY = ${AIRVISUAL_KEY}
ENV POSTGRES_USER = ${POSTGRES_USER}
ENV POSTGRES_PASSWORD = ${POSTGRES_PASSWORD}
ENV POSTGRES_HOST = ${POSTGRES_HOST}
ENV POSTGRES_PORT = ${POSTGRES_PORT}
ENV POSTGRES_DATABASE = ${POSTGRES_DATABASE}
ENV WEATHER_KEY = ${WEATHER_KEY}

CMD ["bash", "-c", "touch /tmp/null.txt && tail -F /tmp/null.txt"]