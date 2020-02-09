FROM python:3

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

ADD . .

RUN apt install git

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt

EXPOSE 8000