import os
import sys

normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))
PROJECT_ROOT = normpath(__file__, "..", "..")

sys.path.append(normpath(PROJECT_ROOT, "apps"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Ondrej Sika', 'sikadev@gmail.com'),
)
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(PROJECT_ROOT, "db", "default.db"),
    }
}
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'cs'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = normpath(PROJECT_ROOT, "static", "uploads")
MEDIA_URL = '/static/uploads/'
STATIC_ROOT = normpath(PROJECT_ROOT, "static", "static")
STATIC_URL = '/static/static/'
STATICFILES_DIRS = (
    normpath(PROJECT_ROOT, "assets"),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
SECRET_KEY = ''
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)
ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'
TEMPLATE_DIRS = (
    normpath(PROJECT_ROOT, "templates"),
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    
    "image_cropping",
    "easy_thumbnails",
    "remote_ajax",
    "bmxacademy",
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
#Default mail settings for gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sikadevmail@gmail.com'
EMAIL_HOST_PASSWORD = 'qayqayqwe'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

NOTIFY_MAIL = "sika.ondrej@gmail.com"

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'easy_thumbnails.processors.filters',
)