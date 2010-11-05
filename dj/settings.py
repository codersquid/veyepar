# Django settings for veyepar project.

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEMPLATE_STRING_IF_INVALID = 'template_error'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

STATICFILES_URL='foo'
# STATICFILES_ROOT='foo'

MANAGERS = ADMINS
DATABASES =  {'default': {'ENGINE': 'django.db.backends.sqlite3',
 'HOST': '',
 'NAME': os.path.join(BASE_DIR,'veyepar.db'),
 'OPTIONS': {},
 'PASSWORD': '',
 'PORT': '',
 'TEST_CHARSET': None,
 'TEST_COLLATION': None,
 'TEST_NAME': None,
 'USER': ''} }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.expanduser('~/Videos/veyepar')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_)n%2id#&ke+^q_si_9c^v(+d9o6$&6kp*&s*w2sl$%esyx4$v'

LOGIN_URL = '/accounts/login'
# LOGIN_REDIRECT_URL = '/main'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    )

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

VALIDATOR_APP_VALIDATORS = {
        'text/html': '/usr/bin/validate',
        'application/xml+xhtml': '/usr/bin/validate',
    }
if False and DEBUG:
    MIDDLEWARE_CLASSES = \
        ('lukeplant_me_uk.django.validator.middleware.ValidatorMiddleware', ) +\
        MIDDLEWARE_CLASSES

ROOT_URLCONF = 'dj.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # BASE_DIR + '/eventcal/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.databrowse',
    'main',
    'accounts',
)

try:    from local_settings import *
except ImportError:    pass

