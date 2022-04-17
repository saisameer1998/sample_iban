# syntax=docker/dockerfile:1

FROM python:3.7.9

ADD . /iban-docker
WORKDIR /iban-docker

RUN pip install -r requirements.txt

CMD [ "python", "main.py"]
