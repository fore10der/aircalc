from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.TextField(max_length=16)