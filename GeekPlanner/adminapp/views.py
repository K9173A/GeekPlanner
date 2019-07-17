"""
Module for adminapp views.
"""
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from plannerapp.models import Project


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class UserListView(ListView):
    """Renders list of all users."""
    template_name = 'adminapp/user_list.html'
    model = User

    def get_queryset(self):
        """
        Get the list of items for this view.
        :return: list of active projects.
        """
        return super(UserListView, self).get_queryset().order_by('id')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class ProjectListView(ListView):
    """Renders list of all projects."""
    template_name = 'adminapp/project_list.html'
    model = Project

    def get_queryset(self):
        """
        Get the list of items for this view.
        :return: list of active projects.
        """
        return super(ProjectListView, self).get_queryset().order_by('id')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['title'] = 'Проекты'
        return context
