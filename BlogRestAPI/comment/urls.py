from django.urls import path
from comment import views

urlpatterns = [
    path('comment/', views.CommentCreateListAPIView.as_view(), name='posts'),
    path('comment/<pk>', views.CommentDetailAPIView.as_view(), name='post-detail'),
]
