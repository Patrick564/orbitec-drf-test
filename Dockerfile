# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

WORKDIR /orbitec_api/

COPY requirements.txt /orbitec_api/

RUN pip install -r requirements.txt

COPY . /orbitec_api/
