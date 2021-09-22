from django.urls import path
from favourite import views



app_name = "favourite"
urlpatterns = [
    path('fav/', views.FavouriteCreateListAPIView.as_view(), name='favs'),
    path('fav/<pk>', views.FavouriteDetailAPIView.as_view(), name='fav-detail'),
]
