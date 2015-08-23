from os import path

import django
from django.conf import settings
from django.test.utils import get_runner


TEST_SETTINGS = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },

    'INSTALLED_APPS': (
        'django.contrib.contenttypes',

        'bigben',
    ),

    'ROOT_URLCONF': 'bigben.urls',
    'BIGBEN_ENABLED': True,
    'DEBUG': True,
    'STATIC_URL': '/static/',
}


def configure():
    settings.configure(**TEST_SETTINGS)
    django.setup()


def run():
    configure()

    runner_class = get_runner(settings)
    runner_class().run_tests(['testsuite'])


if __name__ == '__main__':
    run()
