"""
Django settings for niamoto project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

SITE_ID = 1

ADMINS = (
    ('Dimitri Justeau', 'dimitri.justeau@gmail.com'),
    ('Philippe Birnbaum', 'philippe.birnbaum@cirad.fr'),
)

MANAGERS = ADMINS

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

# Application definition

INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.sites',

    # Third party
    'mptt',
    'rest_framework',
    'rest_framework_gis',
    'constance',
    'constance.backends.database',
    'django_forms_bootstrap',
    'crispy_forms',
    'multiselectfield',
    'dbbackup',
    'explorer',
    'rest_framework_docs',
    'qgis_plugin_repository',

    # Project
    'apps.niamoto_management',
    'apps.niamoto_data',
    'apps.niamoto_plantnote',
    'apps.geoserver_admin',
    'apps.forest_digitizing',
    'apps.rapid_inventories',
    'rest',
    'web',

    # Pinax
    'pinax_theme_bootstrap',
    'bootstrapform',
    'account',
    'pinax.webanalytics',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'niamoto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PACKAGE_ROOT, "templates"), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'account.context_processors.account',
                'pinax_theme_bootstrap.context_processors.theme',
            ],
        },
    },
]

WSGI_APPLICATION = 'niamoto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        'HOST': 'niamoto-postgres',
        'PORT': '5432',
        'NAME': 'niamoto',
        'USER': 'niamoto',
        'PASSWORD': 'niamoto',
    },
    "readonly": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        'HOST': 'niamoto-postgres',
        'PORT': '5432',
        'NAME': 'niamoto',
        'USER': 'niamoto_readonly',
        'PASSWORD': 'niamoto_readonly',
    }
}


# django-dbbackup settings

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_LOCATION = os.path.join(BASE_DIR, 'data', 'backups')
DBBACKUP_STORAGE_OPTIONS = {
    'location': DBBACKUP_LOCATION
}


# Niamoto management settings

MONTHLY_BACKUPS_PATH = os.path.join(DBBACKUP_LOCATION, "monthly")
DAILY_BACKUPS_PATH = os.path.join(DBBACKUP_LOCATION, "daily")
HOURLY_BACKUPS_PATH = os.path.join(DBBACKUP_LOCATION, "hourly")

MAX_MONTHLY_BACKUP_COUNT = 12
MAX_DAILY_BACKUP_COUNT = 31
MAX_HOURLY_BACKUP_COUNT = 24


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = "Pacific/Noumea"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/site_media/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'site_media', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'site_media', 'media')

# Celery settings
CELERY_BROKER = 'amqp://niamoto-rabbitmq:5672//'
CELERY_BACKEND = 'amqp://niamoto-rabbitmq:5672//'


# REST settings
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
}

REST_FRAMEWORK_DOCS = {
    'HIDE_DOCS': False,
    'MODULE_ROUTERS': {},
    'DEFAULT_MODULE_ROUTER': 'router',
    'DEFAULT_ROUTER': None,
}

REST_API_URL_PREFIX = 'api'
REST_API_VERSION = '1.0'
REST_API_BASE_URL = '/'.join((
    REST_API_URL_PREFIX,
    REST_API_VERSION,
))


# Pinax-user-accounts settings
LOGIN_URL = '/account/login/'
ACCOUNT_HOOKSET = "web.hooks.AccountGmailHookSet"
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
THEME_CONTACT_EMAIL = 'dimitri.justeau@gmail.com'


CONSTANCE_CONFIG = {
    # Email configuration
    'DEFAULT_FROM_EMAIL': ('niamoto.nc@gmail.com', 'Default email from'),
    'EMAIL_HOST': ('', 'Email provider host'),
    'EMAIL_HOST_USER': ('', 'Email provider user'),
    'EMAIL_HOST_PASSWORD': ('', 'Email provider password'),
    'EMAIL_PORT': (587, 'Email provider port'),
    'EMAIL_USE_TLS': (True, 'Email use TLS or not'),
    'GEOSERVER_BASE_URL': (
        'http://geoniamoto.ird.nc/geoserver/',
        "Niamoto's geoserver base url"
    ),
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'


# django-sql-explorer settings

EXPLORER_CONNECTION_NAME = "readonly"

EXPLORER_PERMISSION_VIEW = lambda u: u.groups.filter(name='team').exists()

EXPLORER_PERMISSION_CHANGE = EXPLORER_PERMISSION_VIEW

EXPLORER_SCHEMA_EXCLUDE_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.sites',
    'mptt',
    'rest_framework',
    'rest_framework_gis',
    'constance',
    'constance.backends.database',
    'django_forms_bootstrap',
    'crispy_forms',
    'multiselectfield',
    'dbbackup',
    'explorer',
    'pinax_theme_bootstrap',
    'bootstrapform',
    'account',
    'pinax.webanalytics',
)
