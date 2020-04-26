"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _
import environ
from django.conf import settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = environ.Path(__file__) - 2
APPS_DIR = ROOT_DIR.path('/')

# Load operating system environment variables and then prepare to use them
env = environ.Env()

# .env file, should load only in development environment
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)

if READ_DOT_ENV_FILE:
    env_file = str(ROOT_DIR.path('.env'))
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', False)

ALLOWED_HOSTS=[os.environ['DJANGO_ALLOWED_HOSTS']]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'brownbags.apps.BrownbagsConfig',
    'accounts.apps.AccountsConfig',
    'gunicorn',
    'rest_framework',
    'django_cleanup.apps.CleanupConfig',
    'imagekit',
    'storages',
    'compressor',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# for DEBUG
if DEBUG:
    def show_toolbar(request):
        return True

    INSTALLED_APPS += [
        'django_extensions',
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    def show_toolbar(request):
            return True

    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "config.context_processors.google_analytics_key",
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Google Analytics
GOOGLE_ANALYTICS_KEY = os.environ.get('GOOGLE_ANALYTICS_KEY', False)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# for sqlite3
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

# for postgres
DATABASES = {
    'default': {
        'ENGINE': os.environ['POSTGRES_ENGINE'],
        'NAME': os.environ['POSTGRES_DATABASE'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': os.environ['POSTGRES_PORT']
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# locale
# ------------------------------------------------------------------------------
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = [
    ('en', _('English')),
    ('ja', _('Japanese')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'dist/')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'contrib'),
)

STATICFILES_FINDERS = (
    # settings.STATICFILES_DIRSに設定したディレクトリからファイルを読み込む
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # アプリケーションのstaticディレクトリからファイルを読み込みむ
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder', # Django Compress
)

# Django Compress
# https://remotestance.com/blog/1222/#index-1
if 'DJANGO_COMPRESS_ENABLED' in os.environ:
    COMPRESS_ENABLED =  os.environ['DJANGO_COMPRESS_ENABLED']

# AWS S3
# ------------------------------------------------------------------------------
if 'DJANGO_DEFAULT_FILE_STORAGE' in os.environ:
    DEFAULT_FILE_STORAGE = os.environ['DJANGO_DEFAULT_FILE_STORAGE']
    AWS_ACCESS_KEY_ID = os.environ['DJANGO_AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['DJANGO_AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['DJANGO_AWS_STORAGE_BUCKET_NAME']
    AWS_LOCATION = os.environ['DJANGO_AWS_LOCATION']
    AWS_DEFAULT_ACL = None
    AWS_S3_FILE_OVERWRITE = True
    AWS_S3_USE_SSL = True

    S3_URL = 'https://%s.s3.amazonaws.com/%s/' % (AWS_STORAGE_BUCKET_NAME, AWS_LOCATION)
    MEDIA_URL = S3_URL
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media', 'uploads')
    MEDIA_URL = '/uploads/'

# LOGIN
# ------------------------------------------------------------------------------
#LOGIN_URL='/accounts/login'
LOGIN_REDIRECT_URL='/'
LOGOUT_REDIRECT_URL='/'
AUTH_USER_MODEL = 'accounts.User'

# LOGGING
# ------------------------------------------------------------------------------
LOGGING_PATH = os.path.join(BASE_DIR, 'logs')
LOGGING_FILE = 'app.log'

if os.name == 'nt':
    LOGGING = {
        'version': 1,
        'formatters': {
            'all': {
                'format': ':'.join([
                    "[%(levelname)s]",
                    "%(asctime)s",
                    "%(process)d",
                    "%(thread)d",
                    "%(message)s",
                ])
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'all',
            },
        },
        'loggers': {
            'common': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
            'api': {
                'handlers': ['console'],
                'level': 'DEBUG',
            }
        },
    }
else:
    LOGGING = {
        'version': 1,
        'formatters': {
            'all': {
                'format': ':'.join([
                    "[%(levelname)s]",
                    "%(asctime)s",
                    "%(process)d",
                    "%(thread)d",
                    "%(message)s",
                ])
            },
        },
        'handlers': {
            'file_time_rotation': { # 時刻ローテート
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOGGING_PATH, LOGGING_FILE),
                'formatter': 'all',
                'when': 'D',
                'interval': 1,
            },
            'console': { # 標準出力
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'all',
            },
        },
        'loggers': {
            'common': {
                'handlers': ['file_time_rotation', 'console' ],
                'level': 'DEBUG',
            },
            'api': {
                'handlers': ['file_time_rotation', 'console'],
                'level': 'DEBUG',
            },
        },
    }

# GeoDjango on Windows
# ------------------------------------------------------------------------------
if os.name == 'nt':
    import platform
    """
    POSTGRES = r"C:\Program Files\PostgreSQL\10"
    OSGEO4W = r"C:\OSGeo4W"
    if '64' in platform.architecture()[0]:
        OSGEO4W += "64"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W

    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['POSTGRES_ROOT'] = POSTGRES
    os.environ['GDAL_LIBRARY_PATH'] = OSGEO4W + r"\bin"
    os.environ['GEOS_LIBRARY_PATH'] = OSGEO4W + r"\bin"
    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + POSTGRES + r"\bin;" + os.environ['PATH']
    """
    POSTGRES = r"C:\Program Files\PostgreSQL\10"
    OSGEO4W = r"C:\Program Files\QGIS 3.4"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W

    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['POSTGRES_ROOT'] = POSTGRES
    os.environ['GDAL_LIBRARY_PATH'] = OSGEO4W + r"\bin"
    os.environ['GEOS_LIBRARY_PATH'] = OSGEO4W + r"\bin"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + POSTGRES + r"\bin;" + os.environ['PATH']
