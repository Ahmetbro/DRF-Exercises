from django.urls import path
from post import views

urlpatterns = [
    path('post/', views.PostCreateListAPIView.as_view(), name='posts'),
    path('post/<slug>', views.PostDetailAPIView.as_view(), name='post-detail'),
]
