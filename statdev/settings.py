"""
Django settings for statdev project.
Generated by 'django-admin startproject' using Django 1.10.5.
"""
from confy import env, database
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the following in the environment:
DEBUG = env('DEBUG', False)
SECRET_KEY = env('SECRET_KEY')
if not DEBUG:
    ALLOWED_HOSTS = [env('ALLOWED_DOMAIN'), ]
else:
    ALLOWED_HOSTS = ['*']
GIT_COMMIT_DATE = os.popen('git log -1 --format=%cd').read()
# Application definition
AUTH_USER_MODEL = 'accounts.EmailUser'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'reversion',
    'crispy_forms',
    'webtemplate_dbca',
    'django_q',
    'social_django',
    'ledger.accounts',  #  Defines custom user model (duplicate from Ledger project).
    'ledger.address',
    #'accounts',
    'applications',
    'actions',
    'approvals',
    'public',
#    'ajax_upload'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
    'dpaw_utils.middleware.SSOLoginMiddleware',
]
ROOT_URLCONF = 'statdev.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'statdev', 'templates'),
            os.path.join(BASE_DIR, 'applications', 'email')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'statdev.context_processors.template_context',
            ],
        },
    },
]
WSGI_APPLICATION = 'statdev.wsgi.application'
LOGIN_URL = 'login'

AUTHENTICATION_BACKENDS = (
     'social_core.backends.email.EmailAuth',
     'django.contrib.auth.backends.ModelBackend',
)
LOGIN_REDIRECT_URL = 'home_page'
STATIC_CONTEXT_VARS = {}
APPLICATION_VERSION_NO = '0.3'
ALLOWED_UPLOAD_TYPES = [
    'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.ms-word.document.12',
    'application/rtf',
    'application/pdf',
    'image/tiff',
    'image/jpeg',
    'image/gif',
    'image/png',
    'text/csv',
    'text/plain'
]
USER_FIELDS = ['email']
SOCIAL_AUTH_STRATEGY = 'social_django.strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social_django.models.DjangoStorage'
SOCIAL_AUTH_EMAIL_FORM_URL = '/ledger/'
SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'ledger.accounts.mail.send_validation'
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/ledger/validation-sent/'
SOCIAL_AUTH_PASSWORDLESS = True
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['first_name', 'last_name', 'email']
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'ledger.accounts.pipeline.lower_email_address',
    'ledger.accounts.pipeline.logout_previous_session',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    # 'social.pipeline.mail.mail_validation',
    'ledger.accounts.pipeline.mail_validation',
    'ledger.accounts.pipeline.user_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    #'social_core.pipeline.user.user_details'
)

# Email settings
EMAIL_HOST = env('EMAIL_HOST', 'email.host')
EMAIL_PORT = env('EMAIL_PORT', 25)
DEFAULT_FROM_EMAIL = 'DoNotReply@dpaw.wa.gov.au'

# Email settings Ledger
ADMINS = ('asi@dpaw.wa.gov.au',)
EMAIL_HOST = env('EMAIL_HOST', 'email.host')
EMAIL_PORT = env('EMAIL_PORT', 25)
EMAIL_FROM = env('EMAIL_FROM', ADMINS[0])
DEFAULT_FROM_EMAIL = EMAIL_FROM

# Database configuration
DATABASES = {'default': database.config()}


# Password validation
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
LANGUAGE_CODE = 'en-AU'
TIME_ZONE = 'Australia/Perth'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Sensible AU date input formats
DATE_INPUT_FORMATS = (
    '%d/%m/%Y',
    '%d/%m/%y',
    '%d-%m-%Y',
    '%d-%m-%y',
    '%d %b %Y',
    '%d %b, %Y',
    '%d %B %Y',
    '%d %B, %Y',
)


# Static files (CSS, JavaScript, Images)
# Ensure that the media directory exists:
if not os.path.exists(os.path.join(BASE_DIR, 'media')):
    os.mkdir(os.path.join(BASE_DIR, 'media'))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIR = (
     "applications/static",
    "common/static",
)
#STATICFILES_DIR = (
#    os.path.join(BASE_DIR, "applications/static"),
#    os.path.join(BASE_DIR, "common/static"),
#)
 
print STATICFILES_DIR
# Logging settings
# Ensure that the logs directory exists:
if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.mkdir(os.path.join(BASE_DIR, 'logs'))
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'statdev_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'statdev.log'),
            'formatter': 'simple',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['statdev_log'],
            'level': 'INFO'
        },
        'statdev': {
            'handlers': ['statdev_log'],
            'level': 'INFO'
        },
    }
}

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Cache settings.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache_table',
    }
}

# django-q configuration
Q_CLUSTER = {
    'name': 'statutory_dev_cluster',
    'workers': 4,
    'recycle': 100,
    'timeout': 90,
    'retry': 120,
    'queue_limit': 50,
    'bulk': 10,
    'orm': 'default',
}

OSCAR_REQUIRED_ADDRESS_FIELDS = []
