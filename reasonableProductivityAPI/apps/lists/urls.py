from django.urls import path, include
from apps.lists import views


app_name = "lists"
urlpatterns = [
    path('users/<pk>/list', views.ListAPIView.as_view()),
    path('users/<pk>/list/<id>', views.ListDetailAPIView.as_view()),
]
