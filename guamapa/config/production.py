import os
from .common import Common
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Production(Common):
    INSTALLED_APPS = Common.INSTALLED_APPS
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    ALLOWED_HOSTS = ['*.danielrb.dev', '104.248.67.201']
    
    INSTALLED_APPS += ('gunicorn', )

    DB_NAME = os.getenv('POSTGRES_DBNAME')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DB_USER = os.getenv('POSTGRES_USER')

    # print('DB env is:')
    # print(f'DB NAME {DB_NAME}')
    # print(f'DB PASSWORD {DB_PASSWORD}')
    # print(f'DB USER {DB_USER}')

    print('going old school')

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis', 
            'NAME': os.environ.get('POSTGRES_DBNAME', 'postgres'),
            'USER': os.environ.get('POSTGRES_USER', 'user'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'password'),
            'HOST': 'db', #os.environ.get('SQL_HOST', 'localhost'),
            'PORT': '5432' #os.environ.get('SQL_PORT', '5432'),
        }
    }

    # DATABASES = {
    #     'default': dj_database_url.config(
    #         default=f'postgis://${DB_USER}:${DB_PASSWORD}@db:5432/${DB_NAME}',
    #         conn_max_age=int(os.getenv('POSTGRES_CONN_MAX_AGE', 600))
    #     )
    # }

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    # http://django-storages.readthedocs.org/en/latest/index.html
    # INSTALLED_APPS += ('storages',)
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # AWS_ACCESS_KEY_ID = os.getenv('DJANGO_AWS_ACCESS_KEY_ID')
    # AWS_SECRET_ACCESS_KEY = os.getenv('DJANGO_AWS_SECRET_ACCESS_KEY')
    # AWS_STORAGE_BUCKET_NAME = os.getenv('DJANGO_AWS_STORAGE_BUCKET_NAME')
    # AWS_DEFAULT_ACL = 'public-read'
    # AWS_AUTO_CREATE_BUCKET = True
    # AWS_QUERYSTRING_AUTH = False
    # MEDIA_URL = f'https://s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/'

    # https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching#cache-control
    # Response can be cached by browser and any intermediary caches (i.e. it is "public") for up to 1 day
    # 86400 = (60 seconds x 60 minutes x 24 hours)
    # AWS_HEADERS = {
    #     'Cache-Control': 'max-age=86400, s-maxage=86400, must-revalidate',
    # }
