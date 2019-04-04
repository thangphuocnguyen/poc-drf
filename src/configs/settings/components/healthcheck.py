from configs.settings.components.common import INSTALLED_APPS

INSTALLED_APPS += [
    'health_check',                             # required
    'health_check.db',                          # stock Django health checkers
    'health_check.cache',
    'health_check.storage',
    # 'health_check.contrib.celery',              # requires celery
    'health_check.contrib.psutil',              # disk and memory utilization; requires psutil
    # 'health_check.contrib.s3boto_storage',      # requires boto and S3BotoStorage backend
    # 'health_check.contrib.rabbitmq',            # requires RabbitMQ broker
]
