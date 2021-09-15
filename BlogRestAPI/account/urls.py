from django.urls import path
from account import views


app_name = "account"
urlpatterns = [
    path('me/', views.ProfileView.as_view(), name='me'),
    path('change-pw/', views.UpdatePassword.as_view(), name='change-password'),
    path('register/', views.CreateUserView.as_view(), name='register'),
]

