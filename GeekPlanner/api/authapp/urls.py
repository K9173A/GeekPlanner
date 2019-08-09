"""
Module for authapp URLs.
"""
from django.urls import path

from . import views


app_name = 'authapp'

urlpatterns = [
    # path(
    #     'login/',
    #     views.LoginAPIView.as_view(),
    #     name='login'
    # ),
    # path(
    #     'logout/',
    #     views.LoginAPIView.as_view(),
    #     name='logout'
    # ),
    # path(
    #     'accounts/register/',
    #     views.RegistrationAPIView.as_view(),
    #     name='register',
    # ),
]
