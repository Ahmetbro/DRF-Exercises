from django.shortcuts import render
from rest_framework.response import Response
from book import serializers
from book.models import Book, Comment
from book.serializers import BookSerializer, CommentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import get_object_or_404
from book.permissions import IsAdminOrReadOnly, IsCommentOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from book.pagination import SmallPagination, LargePagination

# Create your views here.

class BookListCreateAPIView(ListCreateAPIView):

    queryset = Book.objects.all().order_by('publish_date')
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = LargePagination
    
class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentListCreateAPIView(ListCreateAPIView):
    #queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self): # yalnızca id si verilen kitabın yorumlarını görüntüleyecek
        book_pk = self.kwargs.get('pk') # urls.py daki path içinde int:pk
        book = get_object_or_404(Book, pk=book_pk)     
        return Comment.objects.filter(book=book)

    def perform_create(self, serializer):
        book_pk = self.kwargs.get('pk') # urls.py daki path içinde int:pk
        book = get_object_or_404(Book, pk=book_pk)
        comment_owner = self.request.user
        comments = Comment.objects.filter(book=book, comment_owner=comment_owner)
        if comments.exists():
            raise ValidationError('You cannot comments on a book more than once')
        serializer.save(book=book, comment_owner=comment_owner) # models.py daki comment.comment_owner

class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentOwnerOrReadOnly]
    