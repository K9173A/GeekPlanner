import os
import json

from django.core.management.base import BaseCommand
from django.conf import settings

from authapp.models import User
from plannerapp.models import Project


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

    def handle(self, *args, **options):
        tables = {
            'Project': Project,
            'User': User,
        }

        for option_key, option_value in options.items():
            if option_key in ['verbosity', 'settings', 'pythonpath', 'traceback', 'no_color'] or option_value is None:
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
                        else:
                            table(**item).save()

                elif option_key == 'show':
                    print('Content of "{}":'.format(table_name), table.objects.all())
