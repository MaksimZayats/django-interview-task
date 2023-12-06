from __future__ import annotations

from rest_framework import serializers

from api.credit import models


class _BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        read_only_fields = ("created", "modified")


class CreditRequestSerializer(_BaseSerializer):
    class Meta:
        model = models.CreditRequest
        fields = ("id", "name", "products", "contract", "user", "created")


class ContractSerializer(_BaseSerializer):
    class Meta:
        model = models.Contract
        fields = ("id", "name", "credit_request", "created")
        extra_kwargs = {
            "credit_request": {"required": False},
        }


class ProductSerializer(_BaseSerializer):
    class Meta:
        model = models.Product
        fields = ("id", "name", "manufacturer", "created")


class ManufacturerSerializer(_BaseSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ("id", "name", "created")
