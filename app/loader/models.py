from django.db import models
from gss.settings.base import SOURCE_PATH

class UploadedFile(models.Model):
    uploader = models.CharField(max_length=16)
    file = models.FileField(upload_to=SOURCE_PATH)
    upload_date = models.DateTimeField(auto_now_add=True)