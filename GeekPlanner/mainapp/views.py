from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    """View of the index page."""
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context
