"""
Module for adminapp URLs.
"""
from django.urls import path

from .views import UserListView, ProjectListView


app_name = 'adminapp'

urlpatterns = [
    path(
        'users/',
        UserListView.as_view(),
        name='users'
    ),
    path(
        'projects/',
        ProjectListView.as_view(),
        name='projects'
    ),
]
