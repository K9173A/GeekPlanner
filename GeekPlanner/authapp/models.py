from datetime import timedelta

from django.utils.timezone import now
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.conf import settings


def get_key_expiration_date():
    """
    Gets key expiration date from current moment.
    :return: expiration date.
    """
    return now() + timedelta(hours=48)


class User(AbstractUser):
    """
    User model overrides default model. User contains fields which are needed
    only for authentication purposes.
    """
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=get_key_expiration_date)

    def is_activation_key_expired(self):
        """
        Checks whether the key has expired for the moment or not.
        :return: boolean result of key expiration checking.
        """
        return now() > self.activation_key_expires


class UserProfile(models.Model):
    """
    UserProfile is an account which can be edited by user.
    """
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=settings.USER_AVATARS_DIR, blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()
