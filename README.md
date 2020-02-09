# Customer Management API

## Requirements

- python 3.6.
- django 3
- docker 19.03.5
- docker-compose 1.17.1

## Run the project

Clone project to local folder then go to customer-mangement project

Run
```
docker-compose -f docker/production.yml up -d
```

## Get customers
You can use [postman](https://www.postman.com/) to interact with the APIs

Make a GET request to get all customers
```
127.0.0.1:8000/api/customers/
```

Make a GET request to get customers that have their phone starts with a specific number
```
127.0.0.1:8000/api/customers/?phone=1234567892
```

## Create a customer

Make a POST request to create a customer
```
127.0.0.1:8000/api/customers
```

with a form of
```
name=test
phone=88889999000
```

__Note:__ You must put customer phone with a fixed 11 digit number