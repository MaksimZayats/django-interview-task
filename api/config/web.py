from __future__ import annotations

import logging
from os import getenv
from typing import Any

logger = logging.getLogger(__name__)

# SECURITY WARNING: keep the secret key used in production secret!
_default_secret_key = (
    "django-insecure-2cb-!o^00(qos7$0wf@$ai#h9!^(ov7w6cj%#0ui;o=ulo!83!"  # noqa: S105
)
SECRET_KEY = getenv("SECRET_KEY", default=_default_secret_key)

if _default_secret_key == SECRET_KEY:
    logger.warning("SECRET_KEY is not set!")

ALLOWED_HOSTS = getenv("ALLOWED_HOSTS", "*").split(",")
ALLOWED_HOSTS.append("localhost")

CSRF_TRUSTED_ORIGINS = getenv("CSRF_TRUSTED_ORIGINS", "http://localhost").split(",")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "api.web.urls"

TEMPLATES: list[dict[str, Any]] = [
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

WSGI_APPLICATION = "api.web.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
