from __future__ import annotations

import logging

from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.credit import models, serializers

logger = logging.getLogger(__name__)


class CreditRequestView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = models.CreditRequest.available_objects.all()
    serializer_class = serializers.CreditRequestSerializer


class ContractView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = models.Contract.available_objects.all()
    serializer_class = serializers.ContractSerializer

    @extend_schema(
        description="Get contract by credit request",
        responses={
            200: {
                "type": "array",
                "items": {
                    "type": "integer",
                },
            },
        },
    )
    @action(detail=True, methods=["get"])
    def get_manufacturer_ids(
        self,
        request: Request,  # noqa: ARG002
        pk: int | None = None,
    ) -> Response:
        """Get manufacturer ids for contract."""
        logger.info(
            "Getting manufacturer ids for contract %s",
            pk,
        )

        manufacturer_ids = (
            models.CreditRequest.objects.filter(
                contract__id=pk,
            )
            .values_list(
                "products__manufacturer__id",
                flat=True,
            )
            .distinct()
        )

        return Response(manufacturer_ids)


class ProductView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = models.Product.available_objects.all()
    serializer_class = serializers.ProductSerializer


class ManufacturerView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = models.Manufacturer.available_objects.all()
    serializer_class = serializers.ManufacturerSerializer
