# Generated by Django 2.0.13 on 2019-07-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plannerapp', '0003_auto_20190704_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='content',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(default='project_thumbnails/default-thumbnail.png', upload_to='project_thumbnails', verbose_name='Превью'),
        ),
    ]
