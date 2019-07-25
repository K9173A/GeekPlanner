"""
Module for plannerapp forms.
"""
from django import forms

from .models import Project, Card, Category


class ProjectForm(forms.ModelForm):
    """Form which is being used to create/edit Project."""
    class Meta:
        model = Project
        fields = ('title', 'description', 'thumbnail')

    def __init__(self, *args, **kwargs):
        """
        Restyles form widgets with Twitter Bootstrap classes.
        :param args: additional parameters.
        :param kwargs: additional key-value parameters.
        """
        super(ProjectForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class CardForm(forms.ModelForm):
    """Form which is being used to create/edit Card."""
    class Meta:
        model = Card
        fields = ('title', 'description', 'priority')

    def __init__(self, *args, **kwargs):
        """
        Restyles form widgets with Twitter Bootstrap classes.
        :param args: additional parameters.
        :param kwargs: additional key-value parameters.
        """
        super(CardForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class CategoryForm(forms.ModelForm):
    """Form which is being used to create/edit project Category."""
    class Meta:
        model = Category
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        """
        Restyles form widgets with Twitter Bootstrap classes.
        :param args: additional parameters.
        :param kwargs: additional key-value parameters.
        """
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
