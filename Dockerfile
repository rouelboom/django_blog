FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY personal_blog /personal_blog

WORKDIR /personal_blog

EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password blog-admin

USER blog-admin
ф