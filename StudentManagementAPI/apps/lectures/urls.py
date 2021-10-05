from django.urls import path, include
from rest_framework_nested import routers

from .views import LectureViewSet

router = routers.SimpleRouter()
router.register(r'', LectureViewSet)


urlpatterns = [
    path('', include(router.urls)),
]