from django.urls import path
from account import views

urlpatterns = [
    path('me/', views.ProfileView.as_view(), name='myself'),
]
