from django.urls import path
from favourite import views

urlpatterns = [
    path('fav/', views.FavouriteCreateListAPIView.as_view(), name='favs'),
    path('fav/<slug>', views.FavouriteDetailAPIView.as_view(), name='fav-detail'),
]
