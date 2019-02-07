from django.contrib import admin
from .models import Plane, PlaneCompany, PlaneFlightHours
# Register your models here.
admin.site.register(Plane)
admin.site.register(PlaneCompany)
admin.site.register(PlaneFlightHours)