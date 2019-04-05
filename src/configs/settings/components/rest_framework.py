from configs.settings.components.common import INSTALLED_APPS

INSTALLED_APPS += [
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',  # django-allauth is required by rest_auth
    'allauth.account',
    # 'allauth.socialaccount',
    'rest_auth',
    'rest_auth.registration',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Just for initial
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}
