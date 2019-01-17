from django.db import models

class PlaneCompany(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Plane(models.Model):
    board_number = models.CharField(max_length=16)
    company = models.ForeignKey(PlaneCompany,on_delete=models.CASCADE)

    def __str__(self):
        return self.board_number