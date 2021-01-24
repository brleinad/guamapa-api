from django.test import TestCase
import factory

from ..models import Town
from ...users.models import User
from .factories import TownFactory

class BaseTownTestCase(TestCase):

    def setUpUsers(self):
        self.password = 'megasecurepass123'
        self.admin_email = 'admin@test.ca'
        self.staff_email = 'staff@test.ca'
        self.normal_email = 'normal@test.ca'
        admin_user = User.objects.create_superuser(email=self.admin_email, password=self.password)
        staff_user = User.objects.create_user(email=self.staff_email, password=self.password, is_staff=True, is_active=True)
        normal_user = User.objects.create_user(email=self.normal_email, password=self.password, is_staff=False, is_active=True)