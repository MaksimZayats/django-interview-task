from __future__ import annotations

from rest_framework.routers import SimpleRouter

from api.credit import views

router = SimpleRouter()
router.register("credits", views.CreditRequestView, basename="credit")
router.register("contracts", views.ContractView, basename="contract")
router.register("products", views.ProductView, basename="product")
router.register("manufacturers", views.ManufacturerView, basename="manufacturer")

urlpatterns = [
    *router.urls,
]
