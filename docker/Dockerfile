FROM python:3

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

ADD . .

RUN apt install git

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt

RUN python manage.py migrate

RUN python manage.py seed

EXPOSE 8000