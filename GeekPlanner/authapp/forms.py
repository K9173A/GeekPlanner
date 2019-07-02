import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from authapp.models import User, UserProfile


def generate_activation_key(email):
    """
    Generates activation key from email and random salt.
    :param email: email address string.
    :return: activation key SHA1 hash.
    """
    random_string = str(random.random()).encode('utf-8')
    salt = hashlib.sha1(random_string).hexdigest()[:6]
    return hashlib.sha1((email + salt)).encode('utf-8').hexdigest()


class UserLoginForm(AuthenticationForm):
    """Form which appears when user clicks 'Login' button"""
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(UserCreationForm):
    """Form which appears when user clicks 'Register' button"""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        """
        Saves user to the database.
        :param commit: Commits unsaved model when False.
        :return: instances that have been saved to the database.
        """
        user = super(UserRegisterForm, self).save()
        user.is_active = False
        user.activation_key = generate_activation_key(user.email)
        user.save()
        return user


class UserEditForm(UserChangeForm):
    """Form which appears when user clicks 'Edit' button"""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserProfileEditForm(forms.ModelForm):
    """Form which contains additional information of User to edit."""
    class Meta:
        model = UserProfile
        fields = ('avatar', 'gender')

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
