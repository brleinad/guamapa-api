import os
from .common import Common
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True

    print('using local')
    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS

    # Mail
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Postgres
    DATABASES = {
        'default': dj_database_url.config(
            default='postgis://daniel:supersecretpassword@db:5432/postgres',
            conn_max_age=int(os.getenv('POSTGRES_CONN_MAX_AGE', 600))
        )
    }

    CORS_ORIGIN_WHITELIST = (
        'http://localhost:3000',
    )

