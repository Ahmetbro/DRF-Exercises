from django.urls import path, include
from apps.lists import views


app_name = "lists"
urlpatterns = [
    path('users/<pk>/list', views.ListAPIView.as_view()),
    path('users/<pk>/list/<id>', views.ListDetailAPIView.as_view()),
    path('users/<pk>/list/<id>/items', views.ListItemAPIView.as_view()),
    path('users/<pk>/list/<id>/items/<str:slug>', views.ListItemDetailAPIView.as_view()),
]
