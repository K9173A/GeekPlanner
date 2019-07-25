"""
Module for authapp forms.
"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm

from django_registration.forms import RegistrationForm

from authapp.models import User, UserProfile


class UserLoginForm(AuthenticationForm):
    """Form which appears when user clicks 'Login' button"""
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        """
        Applies Twitter Bootstrap styles to the form fields.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        """
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UserRegistrationForm(RegistrationForm):
    """Form for the two-step user authentication."""
    # Requires to fill the following additional fields of the form:
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta(RegistrationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email',)

    def __init__(self, *args, **kwargs):
        """
        Applies Twitter Bootstrap styles to the form fields.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        """
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UserEditForm(UserChangeForm):
    """Form which appears when user clicks 'Edit' button"""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password',)

    def __init__(self, *args, **kwargs):
        """
        Applies Twitter Bootstrap styles to the form fields.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        """
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UserProfileEditForm(forms.ModelForm):
    """Form which contains additional information of User to edit."""
    class Meta:
        model = UserProfile
        fields = ('avatar', 'gender',)

    def __init__(self, *args, **kwargs):
        """
        Applies Twitter Bootstrap styles to the form fields.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        """
        super(UserProfileEditForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
