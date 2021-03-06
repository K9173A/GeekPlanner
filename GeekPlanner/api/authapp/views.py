"""
Module for authapp views.

We should override default context data, rewriting some data including:
protocol, domain and site name, because by default djoser uses Django
data and, for instance, sets port number to 8000 (default one). We have a
separate application for frontend, so we need to redefine it with
frontend port and address (Vue.js). So, for instance, when user clicks on
the activation link, he will be redirected to the Vue.js component, which then
will send needed data to the backend to complete activation.
"""
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from djoser import utils
from djoser.conf import settings as djoser_settings
from templated_mail import mail

from .serializers import UserSerializer


class ActivationEmailView(mail.BaseEmailMessage):
    """
    View which controls content of the activation message sent to
    the user email, so he can complete activation process.
    """
    template_name = 'email/activation.html'

    def get_context_data(self, **kwargs):
        """
        Overrides context data.
        :param kwargs: additional key-value arguments.
        :return: renewed context.
        """
        context = super(ActivationEmailView, self).get_context_data()
        user = context.get('user')
        context['uid'] = utils.encode_uid(user.pk)
        context['token'] = default_token_generator.make_token(user)
        context['url'] = djoser_settings.ACTIVATION_URL.format(**context)
        context['protocol'] = settings.DJOSER_GEEKPLANNER.get('protocol')
        context['domain'] = settings.DJOSER_GEEKPLANNER.get('domain_address')
        context['site_name'] = settings.DJOSER_GEEKPLANNER.get('domain_name')
        return context


class ConfirmationEmailView(mail.BaseEmailMessage):
    template_name = 'email/confirmation.html'

    def get_context_data(self, **kwargs):
        context = super(ConfirmationEmailView, self).get_context_data()
        context['site_name'] = settings.DJOSER_GEEKPLANNER.get('domain_name')
        return context


class PasswordResetEmailView(mail.BaseEmailMessage):
    template_name = 'email/password_reset.html'

    def get_context_data(self):
        context = super().get_context_data()
        user = context.get('user')
        context['uid'] = utils.encode_uid(user.pk)
        context['token'] = default_token_generator.make_token(user)
        context['url'] = settings.PASSWORD_RESET_CONFIRM_URL.format(**context)
        context['protocol'] = settings.DJOSER_GEEKPLANNER.get('protocol')
        context['domain'] = settings.DJOSER_GEEKPLANNER.get('domain_address')
        context['site_name'] = settings.DJOSER_GEEKPLANNER.get('domain_name')
        return context


class PasswordChangedConfirmationEmail(mail.BaseEmailMessage):
    template_name = "email/password_changed_confirmation.html"

    def get_context_data(self, **kwargs):
        context = super(PasswordChangedConfirmationEmail, self).get_context_data()
        context['site_name'] = settings.DJOSER_GEEKPLANNER.get('domain_name')
        return context


class UsernameChangedConfirmationEmail(mail.BaseEmailMessage):
    template_name = "email/username_changed_confirmation.html"

    def get_context_data(self, **kwargs):
        context = super(UsernameChangedConfirmationEmail, self).get_context_data()
        context['site_name'] = settings.DJOSER_GEEKPLANNER.get('domain_name')
        return context


class UsernameResetEmail(mail.BaseEmailMessage):
    template_name = "email/username_reset.html"

    def get_context_data(self):
        context = super().get_context_data()
        user = context.get('user')
        context['uid'] = utils.encode_uid(user.pk)
        context['token'] = default_token_generator.make_token(user)
        context['url'] = settings.PASSWORD_RESET_CONFIRM_URL.format(**context)
        context['protocol'] = settings.DJOSER_GEEKPLANNER.get('protocol')
        context['domain'] = settings.DJOSER_GEEKPLANNER.get('domain_address')
        context['site_name'] = settings.DJOSER_GEEKPLANNER.get('domain_name')
        return context


class UserProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
