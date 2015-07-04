from setuptools import setup
from distutils.core import Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from django.conf import settings
        settings.configure(
            DATABASES={
                'default': {
                    'NAME': 'test.db',
                    'TEST_NAME': 'test.db',
                    'ENGINE': 'django.db.backends.sqlite3'
                }
            },
            INSTALLED_APPS = (
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.admin',
                'django.contrib.gis',
                'calculate',
            ),
            MIDDLEWARE_CLASSES=(),
        )
        from django.core.management import call_command
        import django
        if django.VERSION[:2] >= (1, 7):
            django.setup()

        # With Django 1.6, the way tests were discovered changed (see
        # https://docs.djangoproject.com/en/1.7/releases/1.6/#new-test-runner)
        # Set the argument to the test management command appropriately
        # depending on the Django version
        test_module = 'calculate.tests'
        if django.VERSION[:2] < (1, 6):
            test_module = 'calculate'

        call_command('test', test_module)


setup(
    name='latimes-calculate',
    version='0.3.0',
    description='Some simple math we use to do journalism.',
    author='Ben Welsh',
    author_email='ben.welsh@latimes.com',
    url='http://github.com/datadesk/latimes-calculate',
    download_url='http://github.com/datadesk/latimes-calculate.git',
    packages=("calculate",),
    cmdclass={'test': TestCommand},
    install_requires=('six>=1.4.1'),
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
