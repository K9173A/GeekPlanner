"""
Module for authapp models.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.conf import settings

from django_registration.signals import user_activated


class User(AbstractUser):
    """Default user model."""


class UserProfile(models.Model):
    """UserProfile is an account which can be edited by user."""
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to=settings.USER_AVATARS_DIR,
        default=settings.DEFAULT_USER_AVATAR
    )
    gender = models.CharField(
        verbose_name='Пол',
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )


@receiver(user_activated)
def save_user_profile(sender, user, request, **kwargs):
    """
    Creates a profile associated with activated User instance.
    Triggered when user_activated signal is being emitted by the ActivationView.
    :param sender: ActivationView subclass used to activate the user.
    :param user: User instance representing the activated account.
    :param request: HttpRequest in which the account was activated.
    :param kwargs: additional key-value arguments.
    :return:
    """
    (user_profile, created) = UserProfile.objects.get_or_create(user=user)
    if created:
        user_profile.save()
