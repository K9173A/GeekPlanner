from django.urls import path

import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    path('users/', adminapp.UserListView.as_view(), name='users'),
]