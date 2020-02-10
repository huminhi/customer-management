#!/bin/bash

while ! curl http://db:5432/ 2>&1 | grep '52'
do
  sleep 1
done

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Seed project with sample data
echo "Seed project with sample data"
python manage.py seed

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000