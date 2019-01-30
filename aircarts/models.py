from django.db import models

class PlaneCompany(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Plane(models.Model):
    board_number = models.CharField(max_length=16)
    company_id = models.ForeignKey(PlaneCompany,on_delete=models.CASCADE)

    def __str__(self):
        return self.board_number

class PlaneFlightHours(models.Model):
    date = models.DateField()
    plane_id = models.ForeignKey(Plane, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.date)