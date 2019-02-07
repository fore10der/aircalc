#!/bin/sh

rm -rf $(find . -name migrations)
python manage.py makemigrations --settings=gss.settings.docker

echo "MIGRATING DATABASE"
python manage.py migrate --settings=gss.settings.docker

echo "COLLECT STATIC"
python manage.py collectstatic --no-input --settings=gss.settings.docker



exec "$@"
