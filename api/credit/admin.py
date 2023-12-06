from __future__ import annotations

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from api.credit import models


@admin.register(models.CreditRequest)
class CreditRequestAdmin(ModelAdmin):
    pass


@admin.register(models.Contract)
class ContractAdmin(ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(ModelAdmin):
    pass


@admin.register(models.Manufacturer)
class ManufacturerAdmin(ModelAdmin):
    pass
