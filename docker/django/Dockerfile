# pull official base image
FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --update curl gcc g++ freetype-dev libjpeg-turbo-dev libpng-dev postgresql-dev \
    && apk add --virtual build-deps musl-dev \
    && rm -rf /var/cache/apk/*

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
COPY ./docker/django/entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x entrypoint.sh
RUN pipenv install --skip-lock --system --dev

# copy project
COPY ./app /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]