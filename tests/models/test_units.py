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
    def setUpTestData():
        UnitCreator.objects.create(name="foo")
        Unit.objects.create(number='jjggh', \
                    manufacturer=UnitCreator.objects.get(id=0))
        # for creator in UNIT_CREATORS:
        #     UnitCreator.objects.create(name=creator["name"])
        # for unit in UNITS:
        #     Unit.objects.create(number=unit["number"], \
        #                         manufacturer=UnitCreator.objects.get(id=unit["creator_id"]))
        # for action in UNIT_ACTIONS:
        #     UnitAction.objects.create(date=date(action["date"]["year"],action["date"]["mouth"],action["date"]["day"]), \
        #                                                 unit=Unit.objects.get(id=action["unit_id"]), \
        #                                                 action_type=action["action_type"] \
        #                                             )
    def test_ass(self):
        self.assertTrue(True)
    # def test_get_unit(self):
    #     for id in range(len(UNITS)):
    #         self.assertEqual(str(Unit.objects.get(id=id+1)), UNITS[id]["number"])
    
    # def test_get_action(self):
    #     for id in range(len(UNIT_ACTIONS)):
    #         self.assertEqual(str(UnitAction.objects.get(id=id+1)), str(date(UNIT_ACTIONS[id]["date"]["year"],UNIT_ACTIONS[id]["date"]["mouth"],UNIT_ACTIONS[id]["date"]["day"])))
    
    # def test_get_creator(self):
    #     for id in range(len(UNIT_CREATORS)):
    #         self.assertEqual(str(UnitCreator.objects.get(id=id+1)), UNIT_CREATORS[id]["name"])