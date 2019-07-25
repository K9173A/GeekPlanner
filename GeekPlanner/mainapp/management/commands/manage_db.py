import os
import json

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction

from authapp.models import User, UserProfile
from plannerapp.models import Project, Category


def load_json_data(file_name):
    """
    Loads data from JSON file.
    :param file_name: file name with extension.
    :return: deserialized JSON data.
    """
    with open(os.path.join(settings.DATA_DIR, file_name), mode='r', encoding='utf-8') as f:
        return json.load(f)


class Command(BaseCommand):
    help = 'Allows to perform different actions on GeekPlanner database.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--empty',
            metavar='table_name',
            nargs='+',
            type=str,
            help='Clears specific table.'
        )
        parser.add_argument(
            '--fill',
            metavar='table_name',
            nargs='+',
            type=str,
            help='Fills specific table with data from JSON file.'
        )
        parser.add_argument(
            '--show',
            metavar='table_name',
            nargs='+',
            type=str,
            help='Shows data of specific table.'
        )
        parser.add_argument(
            '--create-superuser',
            action='store_true',
            help='Creates superuser "admin" in the database.'
        )
        parser.add_argument(
            '--init-categories',
            action='store_true',
            help='Initializes Category with predefined values'
        )

    def handle(self, *args, **options):
        """
        Executes commands by handling specified keys.
        :param args: additional arguments.
        :param options: command keys and values.
        :return: None.
        """
        tables = {
            'Project': Project,
            'User': User,
        }

        for option_key, option_value in options.items():
            if option_key in ['verbosity', 'settings', 'pythonpath', 'traceback', 'no_color']:
                continue

            if option_key == 'create_superuser' and option_value:
                with transaction.atomic():
                    user = User.objects.create_superuser('admin', 'admin@geekplaner.local', 'admin')
                    UserProfile.objects.create(user=user)
                continue

            if option_key == 'init_categories' and option_value:
                Category.objects.get_or_create(name='TO-DO')
                Category.objects.get_or_create(name='Do Today')
                Category.objects.get_or_create(name='In Progress')
                Category.objects.get_or_create(name='Done')

            if option_value is None or option_value is False:
                continue

            for table_name in option_value:
                table = tables.get(table_name, None)
                if table is None:
                    continue

                if option_key == 'empty':
                    content = table.objects.all()
                    if content is None:
                        continue
                    content.delete()

                elif option_key == 'fill':
                    data = load_json_data('{}.json'.format(table_name))
                    for item in data:
                        if table is User:
                            User.objects.create_user(**item)
                        elif table is Project:
                            if 'owner' in item.keys():
                                owner = User.objects.filter(pk=item['owner']).first()
                                item['owner'] = owner if owner else None
                            table(**item).save()

                elif option_key == 'show':
                    print('Content of "{}":'.format(table_name), table.objects.all())
