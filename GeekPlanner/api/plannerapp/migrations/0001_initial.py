# Generated by Django 2.2 on 2019-08-23 14:44

import api.plannerapp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import functools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('description', models.TextField(blank=True, max_length=256, verbose_name='description')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('thumbnail', models.ImageField(blank=True, upload_to='project_thumbnails', verbose_name='thumbnail')),
                ('is_active', models.BooleanField(default=True, verbose_name='activity')),
                ('is_public', models.BooleanField(default=True, verbose_name='public')),
                ('users', models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('is_active', models.BooleanField(default=True, verbose_name='activity')),
                ('projects', models.ManyToManyField(related_name='categories', to='plannerapp.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('description', models.TextField(blank=True, max_length=512, verbose_name='content')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('is_active', models.BooleanField(default=True, verbose_name='activity')),
                ('priority', models.IntegerField(choices=[(0, 'Lowest'), (1, 'Low'), (2, 'Normal'), (3, 'High'), (4, 'Very High'), (5, 'Highest')], default=2, verbose_name='priority')),
                ('category', models.ForeignKey(default=functools.partial(api.plannerapp.models.get_default_category_pk, *(), **{'name': 'TO-DO'}), null=True, on_delete=django.db.models.deletion.SET_NULL, to='plannerapp.Category', verbose_name='category')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plannerapp.Project', verbose_name='project')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_owner', models.BooleanField(default=False, verbose_name='isOwner')),
                ('is_active', models.BooleanField(default=True, verbose_name='activity')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participation', to='plannerapp.Project', verbose_name='project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'unique_together': {('project', 'user')},
            },
        ),
    ]
