from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from plannerapp.models import Project


class ProjectListView(ListView):
    """Renders a list of projects available for current user."""
    model = Project

    def get_queryset(self):
        """
        Get the list of items for this view.
        :return: list of active projects.
        """
        return super().get_queryset().filter(is_active=True).order_by('date_created')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the list of objects.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Проекты'
        return context

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        """
        The view part of the view – the method that accepts a request argument
        plus arguments, and returns a HTTP response. Overrides default one
        and requires login.
        :param request: request object.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: HTTP response.
        """
        return super().dispatch(request, *args, **kwargs)

