from django.test import TestCase
from .models import Unit, UnitCreator

class ModelExistTest(TestCase):
    def setUp(self):
        UnitCreator.objects.create(name="ass")
    def test_get_from_db(self):
        unit_creator = UnitCreator.objects.get(id=1)
        self.assertEqual(unit_creator.name,'ass')