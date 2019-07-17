"""
Module for mainapp views.
"""
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    """View of the index page."""
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context
