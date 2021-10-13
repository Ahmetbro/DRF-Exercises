from django.urls import path, include
from apps.task import views


app_name = "tasks"
urlpatterns = [
    path('users/<pk>/task', views.TaskView.as_view()),
]
