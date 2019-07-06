from django.db import models
from django.conf import settings

from authapp.models import User


class Project(models.Model):
    title = models.CharField(verbose_name='Название', max_length=64)
    description = models.TextField(verbose_name='Описание', max_length=256, blank=True)
    owner = models.ForeignKey(User, verbose_name='Владелец', null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    thumbnail = models.ImageField(verbose_name='Превью', upload_to=settings.PROJECT_THUMBNAIL_DIR, blank=True)
    is_active = models.BooleanField(verbose_name='Активность', default=True)

    def __str__(self):
        return f'{self.title} ({self.date_created})'


class Card(models.Model):
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=64)
    content = models.TextField(verbose_name='Содержимое', max_length=512, blank=True)
    date_created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Активность', default=True)

    def __str__(self):
        return f'{self.title} ({self.date_created})'
