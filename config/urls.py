from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("api/v1/", include("config.api_router"), name="api_router"),
        path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
        path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
        path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
        path(
            "api/v1/docs/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
