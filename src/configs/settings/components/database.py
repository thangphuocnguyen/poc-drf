from configs.settings import autoconfig

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        # Choices are: postgresql_psycopg2, mysql, sqlite3, oracle
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        # Database name or filepath if using 'sqlite3':
        'NAME': autoconfig('DB_NAME', default='DB_NAME'),

        # You don't need these settings if using 'sqlite3':
        'USER': autoconfig('DB_USER', default='DB_USER'),
        'PASSWORD': autoconfig('DB_PASSWORD', default='DB_PASSWORD'),
        'HOST': autoconfig('DB_HOST', default='DB_HOST'),
        'PORT': autoconfig('DB_PORT', cast=int, default=5432),
        'CONN_MAX_AGE': autoconfig('CONN_MAX_AGE', cast=int, default=60),
    },
}
