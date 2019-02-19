from django.db import models
from django.db.models.signals import post_save
from gss.settings.base import SOURCE_PATH
from gss.celery import app
from .utils import preprocess_xlsx, store_to_db

class UploadedFile(models.Model):
    uploader = models.CharField(max_length=16)
    file = models.FileField(upload_to=SOURCE_PATH)
    upload_date = models.DateTimeField(auto_now_add=True)

@app.task(queue='loads')
def xlsx_parse(xlsx_id):
    xlsx = UploadedFile.objects.get(id=xlsx_id)
    data = preprocess_xlsx(xlsx.file)
    store_to_db(data)

def xlsx_load(sender, instance, **kwargs):
    xlsx_parse.delay(instance.id)

post_save.connect(xlsx_load, sender=UploadedFile)