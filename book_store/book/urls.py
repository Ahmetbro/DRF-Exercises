from django.urls import path, include
from book import views


urlpatterns = [
    path('books', views.BookListCreateAPIView.as_view(), name='book info' ),
    path('books/<int:pk>/comments', views.CommentListCreateAPIView.as_view(), name='book comments'),
    path('books/<int:pk>', views.BookDetailAPIView.as_view(), name='book-detail'),
    path('comments/<int:pk>', views.CommentDetailAPIView.as_view(), name='comment-detail'),
]
