from .base import *

DEBUG = True

BROKER_URL = 'redis://localhost:6379'
RESULT_BACKEND = 'redis://localhost:6379'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gss_debug',
        'USER': 'postgres',
        'PASSWORD' : 'postgres',
        'HOST': '127.0.0.1', # set in docker-compose.yml
        'PORT': 5432 # default postgres port
    }
}