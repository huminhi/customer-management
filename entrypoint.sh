#!/bin/bash

# Test database connection
echo "Testing database connection"
python test_db.py

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Seed project with sample data
echo "Seed project with sample data"
python manage.py seed

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000