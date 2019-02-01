from django.db import models

ACTION_TYPES = (
    (0, 'removals'),
    (1, 'failures'),
    (2, 'induced')
)
#Поставщик блока
class UnitCreator(models.Model):
    #Наименование поставщика
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name
#Блок
class Unit(models.Model):
    #Наимиенование блока
    unit_number = models.CharField(max_length=16)
    #Поставщик блока
    manufacturer_id = models.ForeignKey(UnitCreator, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("unit_number", "manufacturer_id"),)

    def __str__(self):
        return self.unit_number
#Событие для блока
class UnitAction(models.Model):
    #Дата события
    date = models.DateField()
    #Имя блока
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE)
    #Тип события
    action_type = models.CharField(max_length=1, choices=ACTION_TYPES)

    def __str__(self):
        return str(self.date)

