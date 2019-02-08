from django.db import models

#Компания производитель воздушного судна
class AircartCompany(models.Model):

    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

#Воздушное судно
class Aircart(models.Model):
    #Номер воздушного судна
    number = models.CharField(max_length=16)
    #Компания производитель
    company = models.ForeignKey(AircartCompany,on_delete=models.CASCADE)

    def __str__(self):
        return self.number

#Часы полета воздуного судна
class AircartFlightRecord(models.Model):
    #Дата полета
    date = models.DateField()
    #ВС
    aircart = models.ForeignKey(Aircart, on_delete=models.CASCADE)
    #Часов в полете
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.date)