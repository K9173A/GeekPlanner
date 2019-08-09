"""
Module for authapp views.
"""

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from djoser import utils
from djoser.conf import settings as djoser_settings
from templated_mail import mail


class ActivationEmailView(mail.BaseEmailMessage):
    template_name = 'email/activation.html'

    def get_context_data(self, **kwargs):
        context = super(ActivationEmailView, self).get_context_data()
        user = context.get('user')
        context['uid'] = utils.encode_uid(user.pk)
        context['token'] = default_token_generator.make_token(user)
        context['url'] = djoser_settings.ACTIVATION_URL.format(**context)
        # Custom frontend settings
        context['protocol'] = settings.DJOSER_GEEKPLANNER.get('protocol')
        context['domain'] = settings.DJOSER_GEEKPLANNER.get('domain_address')
        context['site_name'] = settings.DJOSER_GEEKPLANNER.get('domain_name')
        return context



# class LoginAPIView(APIView):
#     """
#     View which controlls the login form.
#     Provides method(s): GET, POST.
#     """
#     permission_classes = (AllowAny,)
#     serializer_class = UserLoginSerializer
#
#     def post(self, request, *args, **kwargs):
#         """
#         Handles user login request.
#         :param request: request object with login form data.
#         :param args: additional arguments.
#         :param kwargs: additional key-value arguments.
#         :return: Response with user credentials.
#         """
#         user_serializer = UserLoginSerializer(data=request.data)
#         if user_serializer.is_valid(raise_exception=True):
#             return Response(user_serializer.data, status=status.HTTP_200_OK)
#         return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class RegistrationAPIView(APIView):
#     """
#     View which shows and checks registration form.
#     Provides method(s): GET, POST.
#     """
#     permission_classes = (AllowAny,)
#
#     def post(self, request, *args, **kwargs):
#         user = request.data.get('user', None)
#         # Converts `rest_framework.request.Request` to the `django.http.HttpRequest`,
#         # because JWT does not work with REST objects
#         response = obtain_jwt_token(request._request)
#         user_serializer = UserSerializer(data=user)
#         if user_serializer.is_valid(raise_exception=True):
#             user_serializer.save()
#             return Response(user_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(user_serializer.data, status=status.HTTP_400_BAD_REQUEST)
