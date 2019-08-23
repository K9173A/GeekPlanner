"""
Module for plannerapp models.
"""
import functools

from django.db import models
from django.conf import settings

from api.authapp.models import User


def get_default_category_pk(name):
    """
    Gets default category PK
    :param name: name of category
    :return:
    """
    return Category.objects.get_or_create(name=name)[0].pk


class Project(models.Model):
    """
    Project represents a separated functional area, where users collaborate, work with cards
    and boards.
    """
    # Project name
    title = models.CharField(
        verbose_name='title',
        max_length=64
    )
    # Short description of what project is about
    description = models.TextField(
        verbose_name='description',
        max_length=256,
        blank=True
    )
    # Date when project was created
    date_created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True
    )
    # Project preview image (optional) - helps to recognize your project
    thumbnail = models.ImageField(
        verbose_name='thumbnail',
        upload_to=settings.PROJECT_THUMBNAILS_DIR,
        blank=True
    )
    # If project is not active, it was "deleted" by user
    is_active = models.BooleanField(
        verbose_name='activity',
        default=True
    )
    # Public projects are displayed for everybody
    # Private projects are displayed only for collaborators
    is_public = models.BooleanField(
        verbose_name='public',
        default=True
    )
    # Implements Many-To-Many relationship with UserProfile model
    users = models.ManyToManyField(
        User,
        related_name='projects'
    )

    def __str__(self):
        """
        Human-readable project representation.
        :return: string with project title and date when it was created.
        """
        return f'{self.title} ({self.date_created})'


class Participation(models.Model):
    """
    Collects data of projects participants.
    """
    # Project
    project = models.ForeignKey(
        Project,
        verbose_name='project',
        related_name='participation',
        null=True,
        on_delete=models.SET_NULL
    )
    # Project participant
    user = models.ForeignKey(
        User,
        verbose_name='user',
        null=True,
        on_delete=models.SET_NULL,
    )
    # Is this user an owner of this project?
    is_owner = models.BooleanField(
        verbose_name='isOwner',
        default=False,
    )
    # If user leaves, this field will be set to False
    is_active = models.BooleanField(
        verbose_name='activity',
        default=True
    )

    class Meta:
        unique_together = (('project', 'user'),)


class Category(models.Model):
    """
    User-defined category which card can be attached to.
    """
    # Category name
    name = models.CharField(
        verbose_name='name',
        max_length=64
    )
    # If category is not active, it was "deleted" by user
    is_active = models.BooleanField(
        verbose_name='activity',
        default=True
    )
    # Implements Many-To-Many relationship with Project model
    projects = models.ManyToManyField(
        Project,
        related_name='categories'
    )

    def __str__(self):
        """
        Human-readable category representation.
        :return: string with category name.
        """
        return self.name


class Card(models.Model):
    """
    Card represents a simple task or note, or anything that is important.
    """
    LOWEST = 0
    LOW = 1
    NORMAL = 2
    HIGH = 3
    VERY_HIGH = 4
    HIGHEST = 5

    PRIORITY_CHOICES = (
        (LOWEST, 'Lowest'),
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
        (VERY_HIGH, 'Very High'),
        (HIGHEST, 'Highest')
    )

    # A project where card is being stored
    project = models.ForeignKey(
        Project,
        verbose_name='project',
        on_delete=models.CASCADE
    )
    # Card name
    title = models.CharField(
        verbose_name='title',
        max_length=64
    )
    # Card text content
    description = models.TextField(
        verbose_name='content',
        max_length=512,
        blank=True
    )
    # Date when card was created
    date_created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True
    )
    # If card is not active, it was "deleted" by user
    is_active = models.BooleanField(
        verbose_name='activity',
        default=True
    )
    # Level of task importance
    priority = models.IntegerField(
        verbose_name='priority',
        choices=PRIORITY_CHOICES,
        default=NORMAL
    )
    # Task category (status)
    category = models.ForeignKey(
        Category,
        verbose_name='category',
        null=True,
        on_delete=models.SET_NULL,
        default=functools.partial(get_default_category_pk, name='TO-DO')
    )

    def __str__(self):
        """
        Human-readable card representation.
        :return: string with card title and date when it was created.
        """
        return f'{self.title} ({self.date_created})'
