import logging
import os
import vk_api

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'i+acxn5(akgsn!sr4^qgf(^m&*@+g1@u^t@=8s@axc41ml*f=s'

DEBUG = False

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bot'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'vk_bot_template.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vk_bot_template.wsgi.application'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "YOUR_EMAIL"
EMAIL_HOST_PASSWORD = "YOUR_PASSWORD"
EMAIL_USE_SSL = True

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

VK_SECRET_KEY = 'VK_SECRET_KEY'  # TODO: заполнить
VK_GROUP_TOKEN = 'VK_GROUP_TOKEN'  # TODO: заполнить
VK_CONFIRMATION_TOKEN = 'VK_CONFIRMATION_TOKEN'  # TODO: заполнить

INTEGER_GROUP_ID = -1  # TODO: заполнить
BOT_OWNER_USER_ID = -1  # TODO: заполнить

vk_session = vk_api.VkApi(token=VK_GROUP_TOKEN)

logger = logging.getLogger(__name__)
