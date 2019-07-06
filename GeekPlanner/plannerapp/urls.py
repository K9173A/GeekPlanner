from django.urls import path

import plannerapp.views as plannerapp


app_name = 'plannerapp'

urlpatterns = [
    path('projects/', plannerapp.projects, name='projects'),
]