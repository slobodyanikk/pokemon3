"""
Django settings for pokemon2 project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from django.urls import reverse_lazy
from pathlib import Path
from os import environ
from dotenv import load_dotenv

# load_dotenv(dotenv_path=".env.docker")
load_dotenv(dotenv_path=".env.local")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = environ.get('DEBUG') == "True"

ALLOWED_HOSTS = [environ.get('ALLOWED_HOSTS'), 'localhost', 'poke_app']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'social_django',
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

ROOT_URLCONF = 'pokemon2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'pokemon2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": environ.get('DB_NAME'),
        "USER": environ.get('DB_USERNAME'),
        "PASSWORD": environ.get('DB_PASSWORD'),
        "HOST": environ.get('DB_HOST'),
        "PORT": environ.get('DB_PORT'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f"{environ.get('CACHE_TYPE')}://{environ.get('CACHE_REDIS_HOST')}:{environ.get('CACHE_REDIS_PORT')}/{environ.get('CACHE_REDIS_DB')}",
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
MY_EMAIL = os.environ.get('MAIL_EMAIL')
MY_EMAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
EMAIL_SERVER = os.environ.get('MAIL_SERVER')
EMAIL_PORT = os.environ.get('MAIL_PORT')

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # или другой способ хранения сессий, какой вам нужен
SESSION_COOKIE_NAME = 'my_session'  # Название куки для сессии

LOGIN_REDIRECT_URL = reverse_lazy("main:profile")

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
# SOCIAL_AUTH_POSTGRES_JSONFIELD_ENABLED = True

SOCIAL_AUTH_GITHUB_KEY = '79d64f3defb25607e66f'
SOCIAL_AUTH_GITHUB_SECRET = '090e7660699384360b1ce85f242d7c2a8c809475'

SOCIAL_AUTH_URL_NAMESPACE = 'social'