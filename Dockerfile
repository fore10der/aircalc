FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code

RUN pip install pipenv
RUN pipenv install --system

ENTRYPOINT ["/bin/sh", "django-entrypoint.sh"]