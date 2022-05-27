import os
from pathlib import Path

# for heroku
import django_heroku  # !!! LOOK AT THE END OF THE FILE

# end import

from . import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config.SECRET_KEY

DEBUG = True

# IF YOU GIVE PERMISSION EVERY HOST
# ALLOWED_HOSTS = ['*']
# IF YOU WANT USE ONLY YOURSELF
ALLOWED_HOSTS = []

# CORS SETTING
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
# YOU SHOULD ADD TO MIDDLEWARE
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:3000",
    "http://127.0.0.1:9000",
]

# END CORS SETTING


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # REST FRAMEWORK
    'rest_framework',
    'drf_yasg',
    # My apps -> nameapp.apps.NameappConfig
    'theonlyapp.apps.TheonlyappConfig',
    # Точно не знаю для чего!
    'djoser',
    'corsheaders',
    'rest_framework_swagger',

]

MIDDLEWARE = [
    # CORS MUST BE FIRST
    'corsheaders.middleware.CorsMiddleware',
    # END CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# REST FRAMEWORK

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # for backend filter
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],

    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}
# END REST FRAMEWORK

''
# FOR SET CUSTOM USER
# AUTH_USER_MODEL = 'myapp.ownusermodel'
AUTH_USER_MODEL = 'theonlyapp.MyUser'
# END OWN USER MODEL


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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATIC SETTING
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# END STATIC SETTING


# MEDIA SETTING
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# END MEDIA SETTING

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# FOR HEROKU
django_heroku.settings(locals())
