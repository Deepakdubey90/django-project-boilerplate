"""
Django settings for newco project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import dj_database_url

DEBUG = True
# TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.sep.join(os.path.abspath(os.path.dirname(__file__)).split(os.sep)[:-1])

APP_ROOT = os.sep.join(os.path.abspath(os.path.dirname(__file__))\
                     .split(os.sep))

INTERNAL_IPS = (
    "127.0.0.1"
    )


# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, "newco/templates"),
# )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's90=w$eoq*f_y-(7nvz=8ydjx_8#j(kcx20$51=gv@@wh9c0k^'

# TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Setup Database
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL', 'postgres://localhost/newco')),
}
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'newco.apps.clients',
    'newco.apps.profiles',
    'newco.apps.posts',
    'newco.apps.dashboard',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# #     'django.template.loaders.eggs.Loader',
# )


# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.debug',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.request',
#     'django.core.context_processors.media',
#     'django.core.context_processors.static',
#     'django.contrib.messages.context_processors.messages',
# )

ROOT_URLCONF = 'newco.urls'

WSGI_APPLICATION = 'newco.wsgi.application'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "newco/static"),
)

STATIC_URL = "/static/"
MEDIA_URL =  "/media/"
MEDIA_ROOT = os.path.join(os.environ.get("WWW_DIR", PROJECT_ROOT), "media")


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "newco/templates"),
        ],
        # 'TEMPLATE_DEBUG': DEBUG,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

STATIC_ROOT = os.path.join(os.environ.get("WWW_DIR", PROJECT_ROOT), "static")

GEOIP_DATABASE =  APP_ROOT + '/generic/db/GeoLiteCity.dat'
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
SESSION_COOKIE_AGE = 7

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/