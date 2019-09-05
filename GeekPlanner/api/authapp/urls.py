"""
Module for authapp urls.
"""
from django.urls import path

import api.authapp.views as auth_api

app_name = 'authapp'

urlpatterns = [
    path(
        'user_profile/<int:pk>/',
        auth_api.UserProfileRetrieveUpdateDestroyAPIView.as_view(),
        name='user_profile',
    ),
    path(
        'update_profile/<int:pk>/',
        auth_api.UserProfileRetrieveUpdateDestroyAPIView.as_view(),
        name='update_profile',
    ),
]