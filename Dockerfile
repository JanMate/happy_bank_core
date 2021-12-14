FROM python:3.8-alpine

LABEL description="Alpine Linux with Python 3"
LABEL author="Oleksandr6676"
LABEL app="Core app"
LABEL version=1.0.0

RUN adduser -S -D New_user
USER New_user

ENV PYTHONPATH="/usr/local/bin/python;/app/core"

COPY requirements.txt /app/requirements.txt
WORKDIR app
RUN pip install -r requirements.txt
COPY core core

CMD ls

