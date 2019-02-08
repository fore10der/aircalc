from django.test import TestCase
from datetime import date
from units.models import Unit, UnitCreator, UnitAction

class AircartsModelsTests(TestCase):
    def setUpTestData():
        creator = UnitCreator.objects.create(name="cool company")
        unit = Unit.objects.create(number="SCP-228", manufacturer=creator)
        action = UnitAction.objects.create(unit=unit, date=date(2019,11,9), action_type=1)

    def test_get_unity(self):
        self.assertEqual(str(Unit.objects.get(number="SCP-228")), "SCP-228")
    
    def test_get_unit_creator(self):
        self.assertEqual(str(UnitCreator.objects.get(name="cool company")), "cool company")
    
    def test_get_unit_action(self):
        self.assertEqual(str(UnitAction.objects.get(date=date(2019,11,9))), str(date(2019,11,9)))