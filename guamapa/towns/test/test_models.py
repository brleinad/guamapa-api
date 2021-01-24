from django.test import TestCase
import factory

from .base import BaseTownTestCase
from ..models import Town
from .factories import TownModelFactory

class TownsModelTestCase(BaseTownTestCase):


    def setUp(self):
        print("testing town model")
        self.setUpUsers()
        self.town_data = factory.build(dict, FACTORY_CLASS=TownModelFactory)

    def test_can_create_town_model(self):
        # TODO: clean up tests
        # self.client.login(email=self.staff_email, password=self.password)
        Town.objects.create(**self.town_data)
        town = Town.objects.filter(name=self.town_data.get('name')).first()
        self.assertEqual(town.name, self.town_data.get('name'))
        self.assertEqual(town.location, self.town_data.get('location'))
