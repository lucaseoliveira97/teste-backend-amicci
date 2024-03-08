#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations 
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting Units Tests..."
python manage.py test
echo ====================================

echo "Starting Category Data..."
python manage.py loaddata ./api/fixtures/categories.json
echo ====================================

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000