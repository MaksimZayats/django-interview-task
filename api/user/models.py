from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.models import AbstractUser
from django.db import models

if TYPE_CHECKING:
    from api.credit.models import CreditRequest


class User(AbstractUser):
    credit_requests: models.QuerySet[CreditRequest]
