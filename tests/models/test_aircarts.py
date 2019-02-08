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
    def setUp(self):
        self.companies = []
        self.aircarts = []
        self.flight_records = []
        for company in AIRCARTS_COMPANIES:
            self.companies.append(AircartCompany.objects.create(name=company["name"]))
        for aircart in AIRCARTS:
            self.aircarts.append(Aircart.objects.create(number=aircart["number"], \
                                                company=self.companies[aircart["company_id"]-1] \
                                            ))
        for flight_record in AIRCARTS_FLIGHT_RECORDS:
            self.flight_records.append(AircartFlightRecord.objects.create(date=date(flight_record["date"]["year"],flight_record["date"]["mouth"],flight_record["date"]["day"]), \
                                                        aircart=self.aircarts[flight_record["aircart_id"]-1], \
                                                        count=flight_record["count"] \
                                                    ))
    def test_get_aircart(self):
        for id in range(len(self.aircarts)):
            self.assertEqual(Aircart.objects.get(id=id+1), self.aircarts[id])
    
    def test_get_aircart_company(self):
        for id in range(len(self.companies)):
            self.assertEqual(AircartCompany.objects.get(id=id+1), self.companies[id])
    
    def test_get_flight_record(self):
        for id in range(len(self.flight_records)):
            self.assertEqual(AircartFlightRecord.objects.get(id=id+1), self.flight_records[id])