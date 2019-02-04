#!/bin/sh

rm -rf $(find . -name migrations)
python /code/manage.py makemigrations

echo "MIGRATING DATABASE"
python /code/manage.py migrate

echo "RUN"
python /code/manage.py runserver 0.0.0.0:8000


# echo "CREATE ADMIN"
# python /code/manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
