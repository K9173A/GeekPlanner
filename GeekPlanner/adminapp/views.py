from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class UserListView(ListView):
    """Renders list of users."""
    template_name = 'adminapp/user_list.html'
    model = User

    def get_queryset(self):
        """
        Get the list of items for this view.
        :return: list of active projects.
        """
        return super().get_queryset().order_by('id')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class UserCreateView(CreateView):
    model = User
