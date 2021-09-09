from comment.paginations import CommentPagination
from comment.permissions import IsOwnerOrReadOnly
from comment.serializers import CommentCreateSerializer, CommentListSerializer, CommentDetailSerializer
from rest_framework import serializers
from comment.models import Comment
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    pagination_class = CommentPagination
 
    def get_queryset(self):
        queryset = Comment.objects.filter(parent = None)
        query = self.request.GET.get("q")  # list url inde url sonunda ?q=.. yazarak ikinci get isteğini yaptığımızdaki query
        if query:
            queryset = queryset.filter(post = query)
        return queryset

    

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    pagination_class = CommentPagination

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]