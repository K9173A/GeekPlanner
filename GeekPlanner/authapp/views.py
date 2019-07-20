"""
Module for authapp views.
"""
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, RedirectView, TemplateView
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse, reverse_lazy
from django.utils.http import is_safe_url
from django.utils.decorators import method_decorator
from django.db import transaction

from .forms import UserLoginForm, UserEditForm, UserProfileEditForm


class LoginView(FormView):
    """Logs user in."""
    form_class = UserLoginForm
    template_name = 'authapp/login.html'

    def get_success_url(self):
        """
        Determines the URL to redirect to when the form is successfully validated.
        :return: success URL.
        """
        next_url = self.request.GET.get('next')
        if is_safe_url(url=next_url, host=self.request.get_host()):
            return next_url
        return reverse('main:index')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        """
        The view part of the view – the method that accepts a request argument
        plus arguments, and returns a HTTP response.
        :param request: request object.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: HTTP response.
        """
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Validates form.
        :param form: form instance.
        :return: success_url by default.
        """
        login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    """Logs user out"""
    url = reverse_lazy('main:index')

    def get(self, request, *args, **kwargs):
        """
        Handles GET request.
        :param request: request object.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: HTTP response.
        """
        if self.request.user.is_authenticated:
            logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegistrationCompleteView(TemplateView):
    """View for a page which congratulates user with successful registration."""
    template_name = 'django_registration/registration_complete.html'

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(RegistrationCompleteView, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация завершена'
        return context


class RegistrationClosedView(TemplateView):
    """
    View for a page which shows instead of registration form in case of the flag:
    settings.REGISTRATION_OPEN = False
    """
    template_name = 'django_registration/registration_closed.html'

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        context = super(RegistrationClosedView, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация закрыта'
        return context


@method_decorator(login_required, name='dispatch')
class UserUpdateView(FormView):
    """Allows to edit User form."""
    template_name = 'authapp/user_update_form.html'
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        """
        Returns context data for displaying the object.
        :param kwargs: additional key-value arguments.
        :return: context data for the template.
        """
        return {'title': 'Редактирование профиля'}

    def get(self, request, *args, **kwargs):
        """
        Handles GET request.
        :param request: request object.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: HTTP response.
        """
        context = self.get_context_data()
        context['user_form'] = UserEditForm(instance=request.user)
        context['profile_form'] = UserProfileEditForm(instance=request.user.profile)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Handles POST request.
        :param request: request object.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: HTTP response.
        """
        user_form = UserEditForm(
            self.request.POST, self.request.FILES, instance=request.user
        )
        profile_form = UserProfileEditForm(
            self.request.POST, instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user_form.save()
                profile_form.save()
            return HttpResponseRedirect(reverse('main:index'))

        context = self.get_context_data()
        context['user_form'] = user_form
        context['profile_form'] = profile_form

        return render(request, self.template_name, context)
