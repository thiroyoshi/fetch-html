FROM python:alpine

WORKDIR /app
COPY . /app

RUN pip install -e .

ENTRYPOINT [ "fetch" ]