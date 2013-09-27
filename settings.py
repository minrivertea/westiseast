# Django settings for westiseast2 project.

import os
PROJECT_PATH = os.path.abspath(os.path.split(__file__)[0])



DEBUG = False
GA_IS_ON = DEBUG
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Chris West', 'chris@fry-it.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-gb'

SITE_ID = 1


USE_I18N = False
USE_L10N = False


MEDIA_ROOT = os.path.join(PROJECT_PATH, "static")
STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

TEMPLATE_LOADERS = (
    'django_mobile.loader.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'westiseast.blog.context_processors.common',
    'django_mobile.context_processors.flavour',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
)

ROOT_URLCONF = 'westiseast.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates/")
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django_static',
    'blog',
    'sorl.thumbnail',
)


FLAVOURS_TEMPLATE_PREFIX = ''
BASE_TEMPLATE = 'base.html'
BASE_TEMPLATE_MOBILE = 'base_mobile.html'


# django static information
DJANGO_STATIC_SAVE_PREFIX = '/tmp/cache-forever/westiseast'
DJANGO_STATIC_NAME_PREFIX = '/cache-forever/westiseast'
DJANGO_STATIC = True
DJANGO_STATIC_MEDIA_URL = 'http://static.westiseast.co.uk'
MEDIA_URL = '/'

try:
    from local_settings import *
except ImportError:
    pass

