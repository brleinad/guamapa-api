from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from faker import Faker
import factory

from .base import BaseTownTestCase
from ..models import Town
from ...users.models import User
from .factories import TownFactory


class TestTownListTestCase(APITestCase, BaseTownTestCase):
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
        self.client.login(email=self.admin_email, password=self.password)
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_logged_out_fails(self):
        response = self.client.post(self.url, self.town_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_normal_user_fails(self):
        self.client.login(email=self.normal_email, password=self.password)
        response = self.client.post(self.url, self.town_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_staff_user_succeeds(self):
        self.client.login(email=self.staff_email, password=self.password)
        response = self.client.post(self.url, self.town_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        town = Town.objects.get(pk=response.data.get('id'))
        self.assertEqual(town.name, self.town_data.get('name'))
        self.assertJSONEqual(town.location.geojson, self.town_data.get('location'))

    def test_post_request_admin_user_succeeds(self):
        self.client.login(email=self.staff_email, password=self.password)
        response = self.client.post(self.url, self.town_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        town = Town.objects.get(pk=response.data.get('id'))
        self.assertEqual(town.name, self.town_data.get('name'))
        self.assertJSONEqual(town.location.geojson, self.town_data.get('location'))

    def test_post_request_with_valid_town_data(self):
        self.client.login(email=self.staff_email, password=self.password)
        print('town_data is')
        response = self.client.post(self.url, self.town_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        town = Town.objects.get(pk=response.data.get('id'))

        self.assertEqual(town.name, self.town_data.get('name'))
        self.assertJSONEqual(town.location.geojson, self.town_data.get('location'))