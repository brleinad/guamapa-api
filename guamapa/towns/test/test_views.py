from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from faker import Faker
import factory

from ..models import Town
from ...users.models import User
from .factories import TownFactory


class TestTownListTestCase(APITestCase):
    """
    Tests /towns list operations
    """

    def setUp(self):
        print("testing towns")
        self.url = reverse('town-list')
        self.town_data = factory.build(dict, FACTORY_CLASS=TownFactory)
        self.password = 'megasecurepass123'
        self.admin_email = 'admin@test.ca'
        self.staff_email = 'staff@test.ca'
        self.normal_email = 'normal@test.ca'
        admin_user = User.objects.create_superuser(email=self.admin_email, password=self.password)
        staff_user = User.objects.create_user(email=self.staff_email, password=self.password, is_staff=True, is_active=True)
        normal_user = User.objects.create_user(email=self.normal_email, password=self.password, is_staff=False, is_active=True)


    def test_post_request_with_no_data_fails(self):
        self.client.login(email=self.staff_email, password=self.password)
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

    def test_post_request_admin_user_succeeds(self):
        self.client.login(email=self.staff_email, password=self.password)
        response = self.client.post(self.url, self.town_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        town = Town.objects.get(pk=response.data.get('id'))
        self.assertEqual(town.name, self.town_data.get('name'))