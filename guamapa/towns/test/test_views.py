from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from faker import Faker
import factory
import json

from .base import BaseTownTestCase
from ..models import Town
from ...users.models import User
from .factories import TownFactory, AssistantMayorFactory


class TownListTestCase(APITestCase, BaseTownTestCase):
    """
    Tests /towns list operations
    """

    def setUp(self):
        print("testing towns")
        self.setUpUsers()
        self.url = reverse('town-list')
        self.town_data = factory.build(dict, FACTORY_CLASS=TownFactory)

    def test_post_request_with_no_data_fails(self):
        # self.client.login(email=self.staff_email, password=self.password)
        self.authenticate_admin()
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_logged_out_fails(self):
        response = self.client.post(self.url, self.town_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_normal_user_fails(self):
        self.authenticate_normal()
        response = self.client.post(self.url, self.town_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_staff_user_succeeds(self):
        self.authenticate_staff()
        response = self.client.post(self.url, self.town_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        town = Town.objects.get(pk=response.data.get('id'))
        self.assertEqual(town.name, self.town_data.get('name'))
        self.assertJSONEqual(town.location.geojson, self.town_data.get('location'))

    def test_post_request_admin_user_succeeds(self):
        self.authenticate_staff()
        response = self.client.post(self.url, self.town_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        town = Town.objects.get(pk=response.data.get('id'))
        self.assertEqual(town.name, self.town_data.get('name'))
        self.assertJSONEqual(town.location.geojson, self.town_data.get('location'))

    def test_post_request_with_valid_town_data(self):
        self.authenticate_staff()
        response = self.client.post(self.url, self.town_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        town = Town.objects.get(pk=response.data.get('id'))

        #TODO: should check response town not model town
        self.assertEqual(town.name, self.town_data.get('name'))
        self.assertEqual(town.population, self.town_data.get('population'))
        self.assertEqual(town.elevation, self.town_data.get('elevation'))
        self.assertJSONEqual(town.location.geojson, self.town_data.get('location'))

    def test_get_request_returns_town_data(self):
        self.authenticate_staff()
        town0 = factory.build(dict, FACTORY_CLASS=TownFactory)
        town1 = factory.build(dict, FACTORY_CLASS=TownFactory)
        town2 = factory.build(dict, FACTORY_CLASS=TownFactory)
        response = self.client.post(self.url, town0)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        respone = self.client.post(self.url, town1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        respone = self.client.post(self.url, town2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.client.logout()
        self.authenticate_normal()
        response: Respone = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_towns: list = response.json()
        response_towns.sort(key=lambda town: town.get('name'))
        towns = [town0, town1, town2]
        towns.sort(key=lambda town: town.get('name'))

        # print('response towns')
        # print(response_towns)

        # print('towns data')
        # print(towns)
        self.assertEqual(len(response.json()), len(towns))
        #TODO: check all data
        # for town in towns:
        #     self.assertEqual(town.get('name'), response_towns.pop(0).get('name')
        # # self.assertJSONEqual(json.dumps(response_towns), json.dumps(towns))
        # pass



class AssistantMayorTestCase(APITestCase, BaseTownTestCase):

    def setUp(self):
        print("testing towns")
        self.setUpUsers()
        self.town_data = factory.build(dict, FACTORY_CLASS=TownFactory)
        # Town.objects.create(**self.town_data)
        self.url = reverse('assistant-mayor-list')

    def test_post_request_with_mayor_data(self):
        self.authenticate_staff()
        town = factory.build(dict, FACTORY_CLASS=TownFactory)
        response = self.client.post(self.url, town)
        a_mayor_url = reverse('town-assistant-mayor', args=[response.data.get('id')])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        a_mayor = factory.build(dict, FACTORY_CLASS=AssistantMayorFactory)

        print('Mayor is')
        print(a_mayor)
        response = self.client.post(a_mayor_url, a_mayor)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, a_mayor)

