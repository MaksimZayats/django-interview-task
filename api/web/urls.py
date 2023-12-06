from __future__ import annotations

from typing import Any

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path, re_path
from django.views.static import serve
from drf_spectacular.utils import extend_schema
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.config.storage import MEDIA_ROOT, STATIC_ROOT

urlpatterns: list[Any] = [
    path("", lambda _request: redirect("docs/"), name="home"),
    path("admin/", admin.site.urls),
    # region Swagger & Schema
    path(
        "api/v1/schema/",
        extend_schema(exclude=True)(SpectacularAPIView).as_view(),
        name="schema",
    ),
    path(
        "docs/",
        extend_schema(exclude=True)(SpectacularSwaggerView).as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        extend_schema(exclude=True)(SpectacularRedocView).as_view(url_name="schema"),
        name="redoc",
    ),
    # endregion Swagger & Schema
    # region Auth
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    # endregion Auth
    # region Apps
    path("", include("api.credit.urls")),
    # endregion Apps
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": STATIC_ROOT}),
]
