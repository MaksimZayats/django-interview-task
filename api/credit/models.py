from __future__ import annotations

from typing import Any

from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class CreditRequest(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=255, verbose_name="Name of the credit request")

    products: models.ManyToManyField[Product, Any] = models.ManyToManyField(
        "credit.Product",
        verbose_name="Products",
        related_name="credit_requests",
    )

    contract = models.OneToOneField(
        "credit.Contract",
        on_delete=models.CASCADE,
        related_name="credit_request",
    )

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="credit_requests",
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.user} - {self.created}"


class Contract(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=255, verbose_name="Name of the contract")

    credit_request: CreditRequest

    def __str__(self) -> str:
        return self.name


class Product(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=255, verbose_name="Name of the product")

    manufacturer = models.ForeignKey(
        "credit.Manufacturer",
        on_delete=models.CASCADE,
        related_name="products",
    )

    credit_requests: models.QuerySet[CreditRequest]

    def __str__(self) -> str:
        return self.name


class Manufacturer(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=255, verbose_name="Name of the manufacturer")

    products: models.QuerySet[Product]

    def __str__(self) -> str:
        return self.name
