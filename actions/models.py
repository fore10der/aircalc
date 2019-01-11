from django.db import models
from aircarts.models import Aircart

# Create your models here.
class Statistic(models.Model):
    aircart = models.ForeignKey(Aircart, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.PositiveIntegerField()

    class Meta:
        unique_together = (('date', 'aircart'),)
        abstract = True

class FH(Statistic): pass
class Removal(Statistic): pass
class Failture(Statistic): pass
class Included(Statistic): pass

        