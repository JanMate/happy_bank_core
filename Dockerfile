FROM python:3.8-alpine

LABEL description="Alpine Linux with Python 3" \
	  author="Oleksandr6676" \
	  app="Core app" \
      version=1.0.0

RUN adduser -S -D core
USER core

ENV PYTHONPATH="/usr/local/bin/python;/app/core"

WORKDIR app
COPY requirements.txt /app/requirements.txt
COPY core core
RUN pip install -r requirements.txt

CMD ls

