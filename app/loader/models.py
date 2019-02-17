from django.db import models
from django.db.models import signals
from gss.settings.base import SOURCE_PATH
from .utils import preprocess_xlsx, store_to_db


class UploadedFile(models.Model):
    uploader = models.CharField(max_length=16)
    file = models.FileField(upload_to=SOURCE_PATH)
    upload_date = models.DateTimeField(null=True, blank=True)

def xlsx_parse(sender, instance, signal, *args, **kwargs):
    file = instance.file
    data = preprocess_xlsx(file)
    store_to_db(data)

signals.post_save.connect(xlsx_parse, sender=UploadedFile)