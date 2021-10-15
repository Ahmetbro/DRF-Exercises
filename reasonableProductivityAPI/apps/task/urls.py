from django import urls
from django.urls import path, include
from apps.task import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'', views.AllTaskViewset)


app_name = "tasks"
urlpatterns = [
    path('tasks/', include(router.urls)),
    path('users/<pk>/task', views.TaskView.as_view()),
    path('users/<pk>/task/<id>', views.TaskDetailAPIView.as_view()),
]
