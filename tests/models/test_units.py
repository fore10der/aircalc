from django.test import TestCase
import json
from datetime import date
from units.models import Unit, UnitCreator, UnitAction
import os

BASE_DIR =os.path.dirname(os.path.realpath(__file__)) 

UNIT_ACTIONS = json.load(open(os.path.join(BASE_DIR, 'units', 'units_actions.json')))
UNIT_CREATORS = json.load(open(os.path.join(BASE_DIR, 'units', 'units_creators.json')))
UNITS = json.load(open(os.path.join(BASE_DIR, 'units', 'units.json')))


class UnitModelsTests(TestCase):
    def setUp(self):
        self.creators = []
        self.units = []
        self.actions = []
        for creator in UNIT_CREATORS:
            self.creators.append(UnitCreator.objects.create(name=creator["name"]))
        for unit in UNITS:
            self.units.append(Unit.objects.create(number=unit["number"], \
                                                manufacturer=self.creators[unit["creator_id"]-1] \
                                            ))
        for action in UNIT_ACTIONS:
            self.actions.append(UnitAction.objects.create(date=date(action["date"]["year"],action["date"]["mouth"],action["date"]["day"]), \
                                                        unit=self.units[action["unit_id"]-1], \
                                                        action_type=action["action_type"] \
                                                    ))
    def test_get_unit(self):
        for id in range(len(self.units)):
            self.assertEqual(Unit.objects.get(id=id+1), self.units[id])
    
    def test_get_action(self):
        for id in range(len(self.actions)):
            self.assertEqual(UnitAction.objects.get(id=id+1), self.actions[id])
    
    def test_get_creator(self):
        for id in range(len(self.creators)):
            self.assertEqual(UnitCreator.objects.get(id=id+1), self.creators[id])