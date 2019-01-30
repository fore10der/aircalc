from django.db import models

ACTION_TYPES = (
    (0, 'removals'),
    (1, 'failures'),
    (2, 'induced')
)

class UnitCreator(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Unit(models.Model):
    unit_number = models.CharField(max_length=16)
    manufacturer_id = models.ForeignKey(UnitCreator, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("unit_number", "manufacturer_id"),)

    def __str__(self):
        return self.unit_number

class UnitAction(models.Model):
    date = models.DateField()
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=1, choices=ACTION_TYPES)

    def __str__(self):
        return str(self.date)

