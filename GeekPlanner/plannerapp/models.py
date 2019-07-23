"""
Module for plannerapp models.
"""
import os

from django.db import models
from django.conf import settings

from authapp.models import User


class Project(models.Model):
    """
    Project represents a separated functional area, where users collaborate, work with cards
    and boards.
    """
    # Project name
    title = models.CharField(
        verbose_name='Название',
        max_length=64
    )
    # Short description of what project is about
    description = models.TextField(
        verbose_name='Описание',
        max_length=256,
        blank=True
    )
    # Creator of the project
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        null=True,
        on_delete=models.SET_NULL
    )
    # Date when project was created
    date_created = models.DateTimeField(
        verbose_name='Создан',
        auto_now_add=True
    )
    # Project preview image (optional) - helps to recognize your project
    thumbnail = models.ImageField(
        verbose_name='Превью',
        upload_to=settings.PROJECT_THUMBNAILS_DIR,
        blank=True
    )
    # If project is not active, it was "deleted" by user
    is_active = models.BooleanField(
        verbose_name='Активность',
        default=True
    )
    # Public projects are displayed for everybody, private projects
    # are displayed only for project creator and his collaborators
    is_public = models.BooleanField(
        verbose_name='Публичность',
        default=True
    )

    def __str__(self):
        """
        Human-readable project representation.
        :return: string with project title and date when it was created.
        """
        return f'{self.title} ({self.date_created})'

    @property
    def thumbnail_url(self):
        """
        Gets path to the project thumbnail with specified name. if it
        does not exist, then replaces it with default thumbnail.
        :return: path to the project thumbnail.
        """
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url
        return os.path.join(settings.STATIC_URL, 'img', 'default', 'thumbnail.png')


class Card(models.Model):
    """
    Card represents a simple task or note, or anything that is important.
    """
    # A project where card is being stored
    project = models.ForeignKey(
        Project,
        verbose_name='Проект',
        on_delete=models.CASCADE
    )
    # Card name
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=64
    )
    # Card text content
    description = models.TextField(
        verbose_name='Содержимое',
        max_length=512,
        blank=True
    )
    # Date when card was created
    date_created = models.DateTimeField(
        verbose_name='Создан',
        auto_now_add=True
    )
    # If card is not active, it was "deleted" by user
    is_active = models.BooleanField(
        verbose_name='Активность',
        default=True
    )

    def __str__(self):
        """
        Human-readable project representation.
        :return: string with card title and date when it was created.
        """
        return f'{self.title} ({self.date_created})'
