from django.db import models

ACTION_TYPES = (
    (0, 'снятие'),
    (1, 'неисправность'),
)

class UnitCreator(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Unit(models.Model):
    unit_number = models.CharField(max_length=16)
    manufacturer = models.ForeignKey(UnitCreator, on_delete=models.CASCADE)

    def __str__(self):
        return self.unit_number

class UnitAction(models.Model):
    date = models.DateField(auto_now=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=1, choices=ACTION_TYPES)

    def __str__(self):
        return self.date

