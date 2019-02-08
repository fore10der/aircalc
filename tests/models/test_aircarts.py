from django.test import TestCase
import json
from datetime import date
from aircarts.models import Aircart, AircartCompany, AircartFlightRecord
import os

BASE_DIR =os.path.dirname(os.path.realpath(__file__)) 

AIRCARTS_FLIGHT_RECORDS = json.load(open(os.path.join(BASE_DIR, 'aircarts', 'aircarts_fh.json')))
AIRCARTS_COMPANIES = json.load(open(os.path.join(BASE_DIR, 'aircarts', 'aircarts_companies.json')))
AIRCARTS = json.load(open(os.path.join(BASE_DIR, 'aircarts', 'aircarts.json')))


class AircartsModelsTests(TestCase):
    def setUpTestData():
        for company in AIRCARTS_COMPANIES:
            AircartCompany.objects.create(name=company["name"])
        for aircart in AIRCARTS:
            Aircart.objects.create(number=aircart["number"], \
                                    company=AircartCompany.objects.get(id=aircart["company_id"]) \
                                    )
        for flight_record in AIRCARTS_FLIGHT_RECORDS:
            AircartFlightRecord.objects.create(date=date(flight_record["date"]["year"],flight_record["date"]["mouth"],flight_record["date"]["day"]), \
                                                        aircart=Aircart.objects.get(id=flight_record["aircart_id"]), \
                                                        count=flight_record["count"] \
                                                    )
    def test_get_aircart(self):
        for id in range(len(AIRCARTS)):
            self.assertEqual(str(Aircart.objects.get(id=id+1)), AIRCARTS[id]["number"])
    
    def test_get_aircart_company(self):
        for id in range(len(AIRCARTS_COMPANIES)):
            self.assertEqual(str(AircartCompany.objects.get(id=id+1)), AIRCARTS_COMPANIES[id]["name"])
    
    def test_get_flight_record(self):
        for id in range(len(AIRCARTS_FLIGHT_RECORDS)):
            self.assertEqual(str(AircartFlightRecord.objects.get(id=id+1)), str(date(AIRCARTS_FLIGHT_RECORDS[id]["date"]["year"],\
                AIRCARTS_FLIGHT_RECORDS[id]["date"]["mouth"],\
                AIRCARTS_FLIGHT_RECORDS[id]["date"]["day"])))