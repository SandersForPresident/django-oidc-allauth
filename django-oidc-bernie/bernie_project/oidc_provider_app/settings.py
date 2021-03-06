# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import oidc_provider_app
import bernie_project
from bernie_project.oidc_provider_app.extra_scopes.scope_claims import ExtraScopeClaims
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'c14d549c574e4d8cf162404ef0b04598'

DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'oidc_provider_app',
    'oidc_provider',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    'bootstrapform'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# If you are running Django 1.8+, specify the context processors
# as follows:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


ROOT_URLCONF = 'oidc_provider_app.urls'


WSGI_APPLICATION = 'oidc_provider_app.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'DATABASE.sqlite3'),
    }
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


# Custom settings

LOGIN_REDIRECT_URL = '/'


# OIDC Provider settings

SITE_URL = 'http://localhost:8000'
OIDC_RSA_KEY_FOLDER = BASE_DIR

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'oidc_provider': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}


SOCIALACCOUNT_ENABLED = 'allauth.socialaccount' in INSTALLED_APPS

REGISTRATION_ENDPOINT_REQ_TOKEN = False
REGISTRATION_ENDPOINT_ENABLED = True

OIDC_EXTRA_SCOPE_CLAIMS = 'bernie_project.oidc_provider_app.extra_scopes.scope_claims.ExtraScopeClaims'
