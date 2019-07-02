from django.urls import path

import authapp.views as authapp


app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login_user, name='login'),
    path('logout/', authapp.logout_user, name='logout'),
    path('register/', authapp.register_user, name='register'),
    path('edit/', authapp.edit_user, name='edit'),
]