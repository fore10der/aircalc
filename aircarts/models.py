from django.db import models
from companies.models import Company

# Create your models here.
class Aircart(models.Model):
    name = models.CharField(max_length=16)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    