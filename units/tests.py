from django.test import TestCase
from .models import Unit, UnitCreator
from test_pages.specials import is_name_exist, is_source_exist

class ModelExistTest(TestCase):
    def setUp(self):
        UnitCreator.objects.create(name="ass")
    def test_get_from_db(self):
        unit_creator = UnitCreator.objects.get(id=1)
        self.assertEqual(unit_creator.name,'ass')
    def test_check_existed_from_db(self):
        self.assertEqual(is_name_exist("hardbass",UnitCreator),False)
    def test_check_not_existed_from_db(self):
        self.assertEqual(is_name_exist("ass",UnitCreator),True)