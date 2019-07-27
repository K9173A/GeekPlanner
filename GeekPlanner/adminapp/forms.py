"""
Module for adminapp forms.
"""
from django.contrib.auth.forms import UserCreationForm

from authapp.models import User


class UserCreateForm(UserCreationForm):
    """Form which allows admin to create a new user account."""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email',)

    def __init__(self, *args, **kwargs):
        """
        Applies Twitter Bootstrap styles to the form fields.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        """
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
