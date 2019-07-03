from django.test import TestCase

from plannerapp.models import User


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('TestUser', email='test@geekplanner.local', password='test')
        self.user.is_staff = True
        self.user.is_active = True
        self.user.save()

    def testLogin(self):
        self.client.login(username='TestUser', password='test')
