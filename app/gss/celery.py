from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gss.settings.dev')

app = Celery('gss')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()