from django.conf import settings
from rest_framework.routers import DefaultRouter


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = DefaultRouter()

app_name = "api"
urlpatterns = router.urls
