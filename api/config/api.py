from __future__ import annotations

import sys
from distutils.util import strtobool
from os import getenv
from pathlib import Path

# Application definition
INSTALLED_APPS: list[str] = [
    # region Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # endregion Django apps
    # region Third-party apps
    "import_export",
    "rest_framework",
    "drf_spectacular",
    # endregion Third-party apps
    # region Project apps
    "api.user",
    "api.credit",
    # endregion Project apps
]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = strtobool(getenv("DEBUG", default="False"))

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = "en-us"

TIME_ZONE = getenv("TIME_ZONE", default="UTC")
USE_I18N = strtobool(getenv("USE_I18N", default="True"))
USE_TZ = strtobool(getenv("USE_TZ", default="True"))

APPEND_SLASH = True

AUTH_USER_MODEL = "user.User"

SEND_REAL_AI_REQUESTS = strtobool(getenv("SEND_REAL_AI_REQUESTS", default="True"))

IS_IN_MIGRATION = "makemigrations" in sys.argv or "migrate" in sys.argv
