#!/bin/sh

rm -rf $(find . -name migrations)
python manage.py makemigrations

echo "MIGRATING DATABASE"
python manage.py migrate

echo "RUN"
python manage.py runserver 0.0.0.0:8000
