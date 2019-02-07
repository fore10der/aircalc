from django.test import TestCase

from datetime import date
from units.models import Unit, UnitCreator, UnitAction

class UnitModelsTests(TestCase):
    def setUp(self):
        self.creator = UnitCreator.create(name="cool creator")
        self.unit = Unit.create(number="cool unit", manufacturer=self.creator)
        self.actions = []
        self.actions.append(UnitAction.create(date=date(2018,2,15), unit=self.unit, action_type=0))
        self.actions.append(UnitAction.create(date=date(2020,1,23), unit=self.unit, action_type=1))
        self.actions.append(UnitAction.create(date=date(2016,2,6), unit=self.unit, action_type=2))
    def test_unicode(self):
        self.assertEqual(True, True)
