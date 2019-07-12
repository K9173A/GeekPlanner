from django.urls import path, re_path

import authapp.views as authapp


app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.LoginView.as_view(), name='login'),
    path('logout/', authapp.LogoutView.as_view(), name='logout'),
    path('register/', authapp.register_user, name='register'),
    path('edit/', authapp.UserUpdateView.as_view(), name='edit'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', authapp.verify, name='verify'),
]