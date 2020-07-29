FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/rest_api_server

RUN pip install --upgrade pip

COPY requirements.txt /usr/src/rest_api_server
RUN pip install -r requirements.txt

COPY . /usr/src/rest_api_server