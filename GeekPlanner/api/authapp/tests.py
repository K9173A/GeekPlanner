"""
Module for authapp tests.
"""
from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.http import HttpRequest

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework_jwt.views import (
    obtain_jwt_token,
    verify_jwt_token,
    refresh_jwt_token,
)

from .models import User
from .views import RegistrationAPIView

# class UserTestCase(TestCase):
#     """
#     Test case of login system.
#     """
#     def setUp(self):
#         """
#         Creates ordinary user with template credentials.
#         :return: None.
#         """
#         self.user = User.objects.create_user(
#             username='TestUser',
#             email='test@geekplanner.local',
#             password='test'
#         )
#         self.user.is_staff = True
#         self.user.save()
#
#     def testLogin(self):
#         """
#         Tries to log user in the system.
#         :return: None.
#         """
#         self.client.login(username='TestUser', password='test')
#
#     def tearDown(self):
#         """
#         Deletes user.
#         :return: None.
#         """
#         self.user.delete()
#
#
# class JWTTestCase(APITestCase):
#     """
#     Test case of JSON Web Token provided by djangorestframework-jwt package.
#     """
#     def setUp(self):
#         """
#         Creates ordinary user with template credentials.
#         :return: None.
#         """
#         self.user = User.objects.create_user(
#             username='TestUser',
#             email='test@geekplanner.local',
#             password='test'
#         )
#         self.token = None
#
#     def test_obtain_jwt_token(self):
#         """
#         Tests obtaining of JWT token from the djangorestframework-jwt package.
#         :return: None.
#         """
#         request = HttpRequest()
#         request.META['REQUEST_METHOD'] = 'POST'
#         request.POST = {
#             'username': self.user.username,
#             'password': self.user.password
#         }
#         response = obtain_jwt_token(request)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertTrue('token' in response.data)
#         self.token = response.data['token']
#
#
#
#
#     def test_verify_jwt_token(self):
#         """
#         Tests verification of JWT token from the djangorestframework-jwt package.
#         :return: None.
#         """
#         data = {'token': self.token}
#         response = self.client.post(reverse(verify_jwt_token), data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_refresh_jwt_token(self):
#         """
#         Tests refreshing of JWT token from the djangorestframework-jwt package.
#         :return: None.
#         """
#         credentials = {
#             'username': self.user.username,
#             'password': self.user.password
#         }
#         response = self.client.post(reverse(refresh_jwt_token), credentials)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def tearDown(self):
#         """
#         Deletes user.
#         :return: None.
#         """
#         self.user.delete()
#
#
class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_registration(self):
        credentials = {
            'username': 'TestUser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@geekplanner.local',
            'password': 'test',
        }
        request = self.factory.post(reverse('auth:register'), credentials)
        view = RegistrationAPIView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
