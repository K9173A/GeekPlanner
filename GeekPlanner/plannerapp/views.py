"""
Module for plannerapp views.
"""
from django.views.generic import DeleteView, CreateView, UpdateView, DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Project, Card, Category
from .forms import ProjectForm, CardForm, CategoryForm


def get_default_categories():
    """
    Gets list of predefined categories.
    :return: list of predefined Category objects.
    """
    return [
        Category.objects.get_or_create(name=name)[0]
        for name in ['TO-DO', 'Do Today', 'In Progress', 'Done']
    ]


@method_decorator(login_required, name='dispatch')
class ProjectListView(ListView):
    """Renders a list of projects available for the current user."""
    model = Project

    def get_queryset(self):
        """
        Get the list of items for this view.
        :return: list of active projects.
        """
        return super(ProjectListView, self).get_queryset().\
            filter(is_active=True).order_by('date_created')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['title'] = 'Projects'
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
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        context['title'] = 'New project'
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
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Edit project'
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
        context = super(ProjectDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Delete project'
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
        context = super(ProjectDetailView, self).get_context_data(**kwargs)

        categories = self.get_project_categories(kwargs['object'].pk)
        categories_card_list = []
        for category in categories:
            cards = Card.objects.filter(
                Q(project=kwargs['object'].pk) &
                Q(is_active=True) &
                Q(category=category)
            )
            categories_card_list.append(cards)

        context['title'] = 'Project'
        context['categories'] = categories
        context['categories_card_list'] = categories_card_list
        return context

    def get_project_categories(self, project_pk):
        # TODO
        return [
            *get_default_categories(),
            # Category.objects.filter(projects=project_pk),
        ]


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
        context['title'] = 'Add card'
        context['project_pk'] = self.kwargs['project_pk']
        return context

    def form_valid(self, form):
        """
        Validates form.
        :param form: form instance.
        :return: success_url by default.
        """
        form.instance.project = Project.objects.get(pk=self.kwargs['project_pk'])
        form.instance.category = Category.objects.get(pk=self.kwargs['category_pk'])
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
        context['title'] = 'Edit card'
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
        context = super(CardDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Delete card'
        context['project_pk'] = self.kwargs['project_pk']
        return context


@method_decorator(login_required, name='dispatch')
class CategoryCreateView(CreateView):
    """Creates new category (status block) in the project."""
    model = Category
    form_class = CategoryForm

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
        context['title'] = 'Add category'
        context['project_pk'] = self.kwargs['project_pk']
        return context


@method_decorator(login_required, name='dispatch')
class CategoryDeleteView(DeleteView):
    """Deletes category and returns to the project."""
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
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Delete category'
        context['project_pk'] = self.kwargs['project_pk']
        return context
