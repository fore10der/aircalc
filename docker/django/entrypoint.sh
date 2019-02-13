#!/bin/sh

rm -rf $(find . -name migrations)
python manage.py makemigrations --settings=gss.settings.docker
python manage.py makemigrations aircarts reporter units loader --settings=gss.settings.docker

echo "MIGRATING DATABASE"
python manage.py migrate --settings=gss.settings.docker


echo "INIT GROUPS"
python manage.py initgroups --settings=gss.settings.docker

echo "COLLECT STATIC"
rm -r -f static
python manage.py collectstatic --no-input --settings=gss.settings.docker


exec "$@"
