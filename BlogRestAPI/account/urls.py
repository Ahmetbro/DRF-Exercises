from django.urls import path
from account import views

urlpatterns = [
    path('me/', views.ProfileView.as_view(), name='myself'),
    path('change-pw/', views.UpdatePassword.as_view(), name='change-password'),
    path('register/', views.CreateUserView.as_view(), name='register'),
]

