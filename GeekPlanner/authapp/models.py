"""
Module for authapp models.
"""
import os

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
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    # Implements One-To-One relationship with User model
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )
    # User avatar
    avatar = models.ImageField(
        verbose_name='avatar',
        upload_to=settings.USER_AVATARS_DIR,
        blank=True
    )
    # User gender: male or female
    gender = models.CharField(
        verbose_name='gender',
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )

    @property
    def avatar_url(self):
        """
        Gets path to the user avatar with specified name. If it
        does not exist, then replaces it with default avatar.
        :return: path to the user avatar.
        """
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return os.path.join(settings.STATIC_URL, 'img', 'default', 'avatar.png')


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
