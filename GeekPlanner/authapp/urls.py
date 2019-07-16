from django.urls import path, re_path
from django.views.generic.base import TemplateView

from django_registration.backends.activation.views import ActivationView, RegistrationView

import authapp.views as authapp_views
import authapp.forms as authapp_forms


app_name = 'authapp'

urlpatterns = [
    path(
        'login/',
        authapp_views.LoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        authapp_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'edit/',
        authapp_views.UserUpdateView.as_view(),
        name='edit'
    ),
    # Django-registration urls
    path(
        'register/',
        RegistrationView.as_view(
            form_class=authapp_forms.UserRegistrationForm
        ),
        name='django_registration_register'
    ),
    path(
        'register/complete/',
        authapp_views.RegistrationCompleteView.as_view(),
        name='django_registration_complete'
    ),
    path(
        'register/closed/',
        authapp_views.RegistrationClosedView.as_view(),
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