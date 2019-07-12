from django.views.generic import DeleteView, CreateView, UpdateView, DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from plannerapp.models import Project, Card
from plannerapp.forms import ProjectForm, CardForm


@method_decorator(login_required, name='dispatch')
class ProjectListView(ListView):
    """Renders a list of projects available for the current user."""
    model = Project

    def get_queryset(self):
        """
        Get the list of items for this view.
        :return: list of active projects.
        """
        return super().get_queryset().filter(is_active=True).order_by('date_created')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
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
        Returns context data for displaying the object.
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
    """Allows to edit information about project."""
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('planner:projects')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
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

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить проект'
        return context


@method_decorator(login_required, name='dispatch')
class ProjectDetailView(DetailView):
    """Allows to work with project."""
    model = Project

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Проект'
        context['card_list'] = Card.objects.filter(project=kwargs['object'].pk)
        return context


@method_decorator(login_required, name='dispatch')
class CardCreateView(CreateView):
    """Creates a new card."""
    model = Card
    form_class = CardForm

    def get_success_url(self):
        """
        Determines the URL to redirect to when the form is successfully validated.
        :return: success URL.
        """
        return reverse('planner:project_details', args=(self.kwargs['project_pk'],))

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить карточку'
        context['project_pk'] = self.kwargs['project_pk']
        return context

    def form_valid(self, form):
        """
        Validates form.
        :param form: form instance.
        :return: success_url by default.
        """
        form.instance.project = Project.objects.get(pk=self.kwargs['project_pk'])
        return super(CardCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CardUpdateView(UpdateView):
    """Allows to edit card data."""
    model = Card
    form_class = CardForm

    def get_success_url(self):
        """
        Determines the URL to redirect to when the form is successfully validated.
        :return: success URL.
        """
        return reverse('planner:project_details', args=(self.kwargs['project_pk'],))

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование карточки'
        context['project_pk'] = self.kwargs['project_pk']
        return context


@method_decorator(login_required, name='dispatch')
class CardDeleteView(DeleteView):
    """Deletes selected card and returns to the project."""
    model = Card

    def get_success_url(self):
        """
        Determines the URL to redirect to when the form is successfully validated.
        :return: success URL.
        """
        return reverse('planner:project_details', args=(self.kwargs['project_pk'],))

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить карточку'
        context['project_pk'] = self.kwargs['project_pk']
        return context

