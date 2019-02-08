from django.contrib import admin
from .models import Aircart, AircartCompany, AircartFlightRecord
# Register your models here.
admin.site.register(Aircart)
admin.site.register(AircartCompany)
admin.site.register(AircartFlightRecord)