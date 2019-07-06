from django.urls import path, re_path

import authapp.views as authapp


app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login_user, name='login'),
    path('logout/', authapp.logout_user, name='logout'),
    path('register/', authapp.register_user, name='register'),
    path('edit/', authapp.edit_user, name='edit'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', authapp.verify, name='verify'),
]