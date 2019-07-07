from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction

from authapp.models import User
from authapp.forms import UserLoginForm, UserRegisterForm, UserEditForm, UserProfileEditForm


def send_verify_mail(user):
    """
    Sends verification mail to the specific e-mail address.
    :param user: user, receiver of mail.
    :return: boolean result of mail sending.
    """
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    title = f'Подтверждение учётной записи {user.username}'
    message = f'''
        Для подтверждения учётной записи {user.username} на портале {settings.DOMAIN_NAME}
        перейдите по ссылке:\n{settings.DOMAIN_NAME}{verify_link}
    '''
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    """
    Verifies user activation key.
    :param request: request object.
    :param email: user email address.
    :param activation_key: user activation key.
    :return: rendered page.
    """
    try:
        user = User.objects.get(email=email)

        context = {
            'activation_success': False
        }

        if user.activation_key != activation_key:
            context['error'] = f'Ключ "{activation_key}" не является валидным!'
        elif user.is_activation_key_expired():
            context['error'] = f'Ключ "{activation_key}" не является активным!'
        elif user.is_active:
            context['error'] = f'Учётная запись "{email}" уже была активирована!'
        else:
            user.is_active = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            context['activation_success'] = True

        return render(request, 'authapp/verification.html', context)
    except Exception as e:
        return HttpResponseRedirect(reverse('main:index'))


def login_user(request):
    """
    For POST method - logs in user.
    For GET method - shows UserLoginForm.
    :param request: request object.
    :return: rendered page.
    """
    # Если метод POST, то значит пользователь отправил данные формы и хочет войти
    if request.method == 'POST':
        # Данные POST-запроса будут распакованы в форме
        login_form = UserLoginForm(data=request.POST or None)
        # Запускает валидацию данных формы и возвращает булевой результат верности данных
        if login_form.is_valid():
            # Проверяет данные пользователя по каждому Backend-у и возвращает объект
            # User, если данные верны, в ином случае Backend кидает PermissionDenied.
            # Функция возвращает None.
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            # Пропускает только, если пользователь не удалял свой аккаунт (is_active=True)
            if user and user.is_active:
                # Сохраняет ID пользователя в сессию, используя Django Session Framework
                login(request, user)
                # Если следующий адрес имеется...
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                # Если следующий адрес 'next' не был найден, то отказываемся от
                # рендеринга и направляемся снова в urls.py
                return HttpResponseRedirect(reverse('planner:projects'))

    # Если метод GET - то создаём пустую форму
    else:
        login_form = UserLoginForm()

    # Берём из GET-запроса следующий URL, который записан как next='...'
    next_url = request.GET['next'] if 'next' in request.GET.keys() else ''

    context = {
        'title': 'Вход',
        'login_form': login_form,
        'next': next_url
    }

    return render(request, 'authapp/login.html', context)


def logout_user(request):
    """
    Logs out user.
    :param request: request object.
    :return: rendered page.
    """
    # "Забывает пользоватея", очищая текущую сессиию
    logout(request)
    # Отказываемся от рендеринга и переходим на главную страницу
    return HttpResponseRedirect(reverse('main:index'))


def register_user(request):
    """
    For POST method - registers user.
    For GET method - shows UserRegisterForm.
    :param request: request object.
    :return: rendered page.
    """
    if request.method == 'POST':
        # request.FILES - словарь, содержащий все загруженные файлы
        register_form = UserRegisterForm(request.POST, request.FILES)
        # Запускает валидацию данных формы и возвращает булевой результат верности данных
        print(register_form.errors)
        if register_form.is_valid():
            # Сохраняет данные формы в БД
            user = register_form.save()
            # Если отправка подтвердительного письма прошла успешно...
            if send_verify_mail(user):
                # то переходим на главную сраницу
                print('Сообщение подтверждения отправлено!')
                return HttpResponseRedirect(reverse('main:index'))
            # в ином случае отправляемся к форме логина
            print('Ошибка отправки сообщения!')
            return HttpResponseRedirect(reverse('auth:login'))

    # Если метод GET - то создаём пустую форму
    else:
        register_form = UserRegisterForm()

    context = {
        'title': 'Регистрация',
        'register_form': register_form
    }

    return render(request, 'authapp/register.html', context)


@transaction.atomic
def edit_user(request):
    """
    For POST method - updates user profile information.
    For GET method - shows UserEditForm и UserProfileEditForm.
    :param request: request object.
    :return: rendered page.
    """
    # Если POST - пользователь внёс изменения в форму...
    if request.method == 'POST':
        # request.user - объект модели пользователя
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        # request.user.shopuserprofile - через объект модели User переходим к его профилю
        profile_form = UserProfileEditForm(request.POST, instance=request.user.shopuserprofile)
        if edit_form.is_valid():
            # Сохраняем изменения, внесённые пользователем
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.shopuserprofile)

    context = {
        'title': 'Редактирование',
        'edit_form': edit_form,
        'profile_form': profile_form
    }

    return render(request, 'authapp/edit.html', context)
