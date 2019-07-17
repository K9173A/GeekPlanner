"""
Module for authapp URLs.
"""
from django.urls import path, re_path
from django.views.generic.base import TemplateView

from django_registration.backends.activation.views import ActivationView, RegistrationView

from .views import LoginView, LogoutView, UserUpdateView,\
                    RegistrationClosedView, RegistrationCompleteView
from .forms import UserRegistrationForm


app_name = 'authapp'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
    path(
        'edit/',
        UserUpdateView.as_view(),
        name='edit'
    ),
    # Django-registration urls
    path(
        'register/',
        RegistrationView.as_view(
            form_class=UserRegistrationForm
        ),
        name='django_registration_register'
    ),
    path(
        'register/complete/',
        RegistrationCompleteView.as_view(),
        name='django_registration_complete'
    ),
    path(
        'register/closed/',
        RegistrationClosedView.as_view(),
        name='django_registration_closed'
    ),
    path(
        'activate/complete/',
        TemplateView.as_view(
            template_name='django_registration/activation_complete.html'
        ),
        name='django_registration_activation_complete'
    ),
    re_path(
        r'^activate/(?P<activation_key>[-:\w]+)/$',
        ActivationView.as_view(),
        name='django_registration_activate'
    ),
]
