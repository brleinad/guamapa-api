from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
import factory

from ..models import Town
from .factories import TownFactory


class TestTownTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('town-list')
        self.town_data = factory.build(dict, FACTORY_CLASS=TownFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.town_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        town = Town.objects.get(pk=response.data.get('id'))
        self.assertEqual(town.name, self.town_data.get('name'))