"""
Module for plannerapp models which should be registered in the admin.
"""
from django.contrib import admin
from .models import Project


admin.site.register(Project)
