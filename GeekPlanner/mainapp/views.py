"""
Module for mainapp views.
"""
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    """Index page view."""
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Main'
        return context


class PricingView(TemplateView):
    """Pricing page view."""
    template_name = 'mainapp/pricing.html'

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(PricingView, self).get_context_data(**kwargs)
        context['title'] = 'Pricing'
        return context
