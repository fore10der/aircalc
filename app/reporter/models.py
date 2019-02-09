from django.db import models
from gss.settings.base import REPORT_PATH

class ReportedFile(models.Model):
    reporter = models.CharField(max_length=16)
    file = models.FilePathField(upload_to=REPORT_PATH)
    generate_date = models.DateField(auto_now_add=True)
    report_date_start = models.DateField()
    report_date_end = models.DateField()
