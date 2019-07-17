"""
Module for authapp tests.
"""
from django.test import TestCase

from plannerapp.models import User


class UserTestCase(TestCase):
    """
    Test case of login system.
    """
    def setUp(self):
        """
        Creates ordinary user with template credentials.
        :return: None.
        """
        self.user = User.objects.create_user(
            'TestUser',
            email='test@geekplanner.local',
            password='test'
        )
        self.user.is_staff = True
        self.user.is_active = True
        self.user.save()

    def testLogin(self):
        """
        Tries to log user in the system.
        :return: None.
        """
        self.client.login(username='TestUser', password='test')
