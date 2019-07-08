from django.views.generic import DeleteView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from plannerapp.models import Project
from plannerapp.forms import ProjectForm


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class ProjectCreateView(CreateView):
    """Creates a new project."""
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('planner:projects')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the list of objects.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новый проект'
        return context

    def form_valid(self, form):
        """
        Validates form.
        :param form: form instance.
        :return: success_url by default.
        """
        form.instance.owner = self.request.user
        return super(ProjectCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProjectUpdateView(UpdateView):
    """Allows to edit information about project"""
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('planner:projects')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the list of objects.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование проекта'
        return context


@method_decorator(login_required, name='dispatch')
class ProjectDeleteView(DeleteView):
    """Deletes selected project and returns to the updated list."""
    model = Project
    success_url = reverse_lazy('planner:projects')


