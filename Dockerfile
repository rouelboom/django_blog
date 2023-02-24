FROM python:3.11-alpine3.17

COPY requirements.txt /temp/requirements.txt
COPY personal_blog /personal_blog

WORKDIR /personal_blog

EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password blog-admin

USER blog-admin
