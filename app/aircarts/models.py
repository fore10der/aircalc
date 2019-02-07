from django.db import models

#Компания производитель воздушного судна
class PlaneCompany(models.Model):

    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

#Воздушное судно
class Plane(models.Model):
    #Номер воздушного судна
    number = models.CharField(max_length=16)
    #Компания производитель
    company = models.ForeignKey(PlaneCompany,on_delete=models.CASCADE)

    def __str__(self):
        return self.board_number

#Часы полета воздуного судна
class PlaneFlightHours(models.Model):
    #Дата полета
    date = models.DateField()
    #ВС
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    #Часов в полете
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.date)