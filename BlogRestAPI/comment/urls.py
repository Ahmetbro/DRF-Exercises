from django.urls import path
from comment import views

urlpatterns = [
    path('create/', views.CommentCreateAPIView.as_view(), name='create'),
    path('list/', views.CommentListAPIView.as_view(), name='list'),
    path('list/<pk>', views.CommentDetailAPIView.as_view(), name='post-detail'),
]
