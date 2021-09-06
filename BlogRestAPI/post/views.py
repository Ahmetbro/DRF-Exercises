from post.permissions import IsOwnerOrReadOnly
from django.shortcuts import render
from post.serializers import PostSerializer
from post.models import Post
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class PostCreateListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)
