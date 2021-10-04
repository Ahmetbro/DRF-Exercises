from django.urls import path, include
from rest_framework_nested import routers

from .views import CertificateViewSet

router = routers.SimpleRouter()
router.register(r'', CertificateViewSet)


urlpatterns = [
    path('', include(router.urls)),
]