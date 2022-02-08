FROM python:3

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install -e .

CMD fetch
