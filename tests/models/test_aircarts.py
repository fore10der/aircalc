from django.test import TestCase
import json
from datetime import date
from aircarts.models import Aircart, AircartCompany, AircartFlightRecord
import os

class AircartsModelsTests(TestCase):
    def setUpTestData():
        company = AircartCompany.objects.create(name="cool company")
        aircart = Aircart.objects.create(number="SCP-228", company=company)
        flight_record = AircartFlightRecord.objects.create(aircart=aircart, date=date(2019,11,9), count=123)

    def test_get_aircart(self):
        self.assertEqual(str(Aircart.objects.get(number="SCP-228")), "SCP-228")
    
    def test_get_aircart_company(self):
        self.assertEqual(str(AircartCompany.objects.get(name="cool company")), "cool company")
    
    def test_get_flight_record(self):
        self.assertEqual(str(AircartFlightRecord.objects.get(date=date(2019,11,9))), str(date(2019,11,9)))