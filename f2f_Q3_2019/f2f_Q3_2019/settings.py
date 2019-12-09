"""
Django settings for f2f_Q3_2019 project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import redis

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
try:
    DEBUG = os.environ["DEBUG"].title() == "True"
except (
    AttributeError,
    KeyError,
):
    DEBUG = False

try:
    ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(",")
except KeyError:
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "graphene_django",
    "core",
    "api",
    "tracker",
]

GRAPHENE = {"SCHEMA": "api.v1.GRAPH.schema.schema"}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = "f2f_Q3_2019.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "f2f_Q3_2019.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}


# http://docs.celeryproject.org/en/latest/userguide/configuration.html
CELERY_BROKER_URL = "amqp://{user}:{password}@{host}:{port}//".format(
    user=os.environ.get("RABBITMQ_DEFAULT_USER"),
    password=os.environ.get("RABBITMQ_DEFAULT_PASS"),
    host=os.environ.get("RABBITMQ_HOST"),
    port=os.environ.get("RABBITMQ_PORT"),
)

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_DB = os.environ.get("REDIS_DB")
# REDIS_NOTIFICATION_KEY = 'notification_send:{type}:id_{id}:{ISO_localtime}'
# REDIS_NOTIFICATION_VALUE = 'MARKED_AS_SEND'
REDIS_CLIENT = redis.StrictRedis(REDIS_HOST, REDIS_PORT, REDIS_DB)

CELERY_RESULT_BACKEND = "redis://@{redis_host}:{redis_port}/{redis_db}".format(
    redis_host=REDIS_HOST, redis_port=REDIS_PORT, redis_db=REDIS_DB,
)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.environ.get("STATIC_ROOT")
MEDIA_ROOT = os.environ.get("MEDIA_ROOT")

# N2YO Config
N2YO_BASE_URL_V1 = "https://www.n2yo.com/rest/v1/satellite/"
N2YO_API_KEY_V1 = os.environ.get("N2YO_API_KEY_V1")
