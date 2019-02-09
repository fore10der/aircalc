from django.db import models
from gss.settings.base import REPORT_PATH

class UploadedFile(models.Model):
    uploader = models.CharField(max_length=16)
    file = models.FileField(upload_to=REPORT_PATH)
    upload_date = models.DateField(auto_now_add=True)
