"""
Module for mainapp URLs.
"""
from django.urls import path

from .views import IndexView, PricingView


app_name = 'mainapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pricing/', PricingView.as_view(), name='pricing'),
]
