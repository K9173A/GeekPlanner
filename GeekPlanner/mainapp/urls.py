"""
Module for mainapp URLs.
"""
from django.urls import path

from .views import IndexView


app_name = 'mainapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
