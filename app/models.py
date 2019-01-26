from django.db import models

class table_data(models.Model):
    Customer = models.IntegerField(max_length=7)
    FH = models.IntegerField(max_length=7)
    NURn = models.IntegerField(max_length=7)
    NFn = models.IntegerField(max_length=7)
    NR = models.IntegerField(max_length=7)
