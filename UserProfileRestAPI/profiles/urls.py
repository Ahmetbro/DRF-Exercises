from django.urls import path, include
from profiles import views

urlpatterns = [
    path('user-profiles/', views.ProfileList.as_view(), name='profiles'),
    
]