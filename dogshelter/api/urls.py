from django.urls import path, include
from api import views


urlpatterns = [
    path('dog/', views.DogList.as_view(), name='dogs'),
    path('dog/<int:pk>/', views.DogDetail.as_view(), name='dog-detail'),
    path('breed/', views.BreedList.as_view(), name='breed-names'),
    path('breed/<int:pk>/', views.BreedDetail.as_view(), name='breed-detail'),
]
