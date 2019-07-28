"""
Module for adminapp views.
"""
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, DeleteView, UpdateView, FormView, DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.db import transaction

from adminapp.forms import UserCreateForm
from authapp.models import User
from authapp.forms import UserEditForm, UserProfileEditForm
from plannerapp.models import Project, Category
from plannerapp.forms import ProjectForm, CategoryForm


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
        return super(UserListView, self).get_queryset()\
            .filter(is_superuser=False).order_by('id')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Users'
        context['create_url'] = reverse('admin:create_user')
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class UserCreateView(CreateView):
    """
    Creates user without a need of authentication via activation link.
    This functionality is allowed ONLY for administrators and superusers who have
    an access to the admin board.
    """
    template_name = 'adminapp/user_form.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('admin:users')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create user'
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class UserReadView(DetailView):
    template_name = 'adminapp/user_detail.html'
    model = User

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(UserReadView, self).get_context_data(**kwargs)
        context['title'] = 'User information'
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class UserUpdateView(FormView):
    """Allows to edit User form."""
    template_name = 'adminapp/user_update_form.html'
    success_url = reverse_lazy('admin:users')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        return {'title': 'Update user'}

    def get(self, request, *args, **kwargs):
        """
        Handles GET request.
        :param request: request object.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: HTTP response.
        """
        context = self.get_context_data()
        user = User.objects.get(pk=kwargs['pk'])
        context['user_form'] = UserEditForm(instance=user)
        context['profile_form'] = UserProfileEditForm(instance=user.profile)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Handles POST request.
        :param request: request object.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: HTTP response.
        """
        user = User.objects.get(pk=kwargs['pk'])

        user_form = UserEditForm(
            self.request.POST,
            self.request.FILES,
            instance=user
        )
        profile_form = UserProfileEditForm(
            self.request.POST,
            instance=user.profile,
        )

        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user_form.save()
                profile_form.save()
            return HttpResponseRedirect(reverse('admin:users'))

        context = self.get_context_data()
        context['user_form'] = user_form
        context['profile_form'] = profile_form

        return render(request, self.template_name, context)


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class UserDeleteView(DeleteView):
    """Deletes selected user and returns to the updated list."""
    template_name = 'adminapp/user_confirm_delete.html'
    model = User
    success_url = reverse_lazy('admin:users')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Delete user'
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
        context['title'] = 'Projects'
        context['create_url'] = reverse('admin:create_project')
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class ProjectCreateView(CreateView):
    """Creates a new project."""
    template_name = 'adminapp/project_form.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('admin:projects')

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


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class ProjectUpdateView(UpdateView):
    """Allows to edit information about project."""
    template_name = 'adminapp/project_update_form.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('admin:projects')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Edit project'
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class ProjectDeleteView(DeleteView):
    """Deletes selected project and returns to the updated list."""
    template_name = 'adminapp/project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('admin:projects')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(ProjectDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Delete project'
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class CategoryListView(ListView):
    """Renders list of all categories."""
    template_name = 'adminapp/category_list.html'
    model = Category

    def get_queryset(self):
        """
        Get the list of items for this view.
        :return: list of active projects.
        """
        return super(CategoryListView, self).get_queryset().order_by('name')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Categories'
        context['create_url'] = reverse('admin:create_category')
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class CategoryCreateView(CreateView):
    form_class = CategoryForm

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create category'
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class CategoryUpdateView(UpdateView):
    pass


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class CategoryDeleteView(DeleteView):
    """Deletes selected category and returns to the updated list."""
    template_name = 'adminapp/category_confirm_delete.html'
    model = Category
    success_url = reverse_lazy('admin:projects')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Delete category'
        return context
