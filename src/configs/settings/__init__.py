"""
Settings main file.

Default environment is `developement`.
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""
from os import environ

from pathlib import PurePath
from decouple import AutoConfig
from split_settings.tools import optional, include


# Build paths inside the project like this: BASE_DIR.joinpath('some')
# `pathlib` is better than writing: dirname(dirname(dirname(__file__)))
BASE_DIR = PurePath(__file__).parent.parent.parent
PROJECT_DIR = BASE_DIR.parent

# Managing environment via DJANGO_ENV variable:
# AutoConfig still able to config this variable but this is an exeption
# since OS environment is more flexible on init app
environ.setdefault('DJANGO_ENV', 'development')

ENV = environ['DJANGO_ENV']

# Loading `.env` files
# See docs: https://gitlab.com/mkleehammer/autoconfig
# Find the .env or .ini file on loading configs
autoconfig = AutoConfig(search_path=PROJECT_DIR)

base_settings = [
    'components/common.py',  # standard django settings
    'components/database.py',  # postgres
    'components/logging.py',
    # 'components/rq.py',  # redis and redis-queue
    'components/emails.py',  # smtp
    'components/csp.py',
    'components/cache.py',
    'components/healthcheck.py',
    'components/rest_framework.py',
    
    # # You can even use glob:
    # # 'components/*.py'
    # Local App Register
    'components/apps_register.py',
    
    # Select the right env:
    'environments/{}.py'.format(ENV),
    # # Optionally override some settings:
    optional('environments/local.py'),
]

# Include settings:
include(*base_settings)
