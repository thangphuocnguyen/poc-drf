"""
This file contains all the settings that defines the development environment.
SECURITY WARNING: don't run with debug turned on in production!
"""
import logging

from configs.settings import autoconfig
from configs.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# Setting the development status:
# Enabled: 
# + django-debug-toolbar
# + nplusone
# + django-querycount

DEBUG = True

ALLOWED_HOSTS = [
    autoconfig('DOMAIN_NAME'),
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
    '[::1]',
]

# -----------------------------------------------------------------------------
# Django debug toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/
# nplusone is a library for detecting the n+1 queries problem 
# in Python ORMs, including SQLAlchemy, Peewee, and the Django ORM
# https://github.com/jmcarp/nplusone
INSTALLED_APPS += (
    'debug_toolbar',
    'nplusone.ext.django',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # https://github.com/bradmontgomery/django-querycount
    # Prints how many queries were executed, useful for the APIs.
    'querycount.middleware.QueryCountMiddleware',
)


def custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK':
        'configs.settings.environments.development.custom_show_toolbar',
}

# This will make debug toolbar to work with django-csp,
# since `ddt` loads some scripts from `ajax.googleapis.com`:
# CSP_SCRIPT_SRC = ("'self'", 'ajax.googleapis.com')
# CSP_IMG_SRC = ("'self'", 'data:')

# -----------------------------------------------------------------------------
# nplusone
# https://github.com/jmcarp/nplusone

MIDDLEWARE += ('nplusone.ext.django.NPlusOneMiddleware',)

# Logging N+1 requests:
NPLUSONE_RAISE = True  # comment out if you want to allow N+1 requests
NPLUSONE_LOGGER = logging.getLogger('django')
NPLUSONE_LOG_LEVEL = logging.WARN
