from django.urls import reverse
from django.contrib.auth.hashers import check_password
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
import factory

from ..models import User
from .factories import UserFactory

fake = Faker()


class TestUserListTestCase(APITestCase):
    """
    Tests /users list operations.
    """

    def setUp(self):
        self.url = reverse('user-list')
        self.user_data = factory.build(dict, FACTORY_CLASS=UserFactory)
        self.password = 'megasecurepass123'
        self.staff_email = 'staff@test.ca'
        staff_user = User.objects.create_user(email=self.staff_email, password=self.password, is_staff=True, is_active=True)

    def test_post_request_logged_out_fails(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_with_no_data_fails(self):
        self.client.login(email=self.staff_email, password=self.password)
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        self.client.login(email=self.staff_email, password=self.password)
        response = self.client.post(self.url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(pk=response.data.get('id'))
        self.assertEqual(user.email, self.user_data.get('email'))
        self.assertEqual(user.email, str(user))
        self.assertTrue(check_password(self.user_data.get('password'), user.password))

    def test_put_request_from_another_user_fails(self):
        # TODO
        pass

    def test_put_request_from_owner_succeeds(self):
        # TODO
        pass


class TestUserDetailTestCase(APITestCase):
    """
    Tests /users detail operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.url = reverse('user-detail', kwargs={'pk': self.user.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

    def test_get_request_returns_a_given_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_request_updates_a_user(self):
        new_first_name = fake.first_name()
        payload = {'first_name': new_first_name}
        response = self.client.put(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = User.objects.get(pk=self.user.id)
        self.assertEqual(user.first_name, new_first_name)
