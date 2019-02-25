from .base import *

DEBUG = False

BROKER_URL = 'redis://redis:6379'
RESULT_BACKEND = 'redis://redis:6379'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db', # set in docker-compose.yml
        'PORT': 5432 # default postgres port
    }
}