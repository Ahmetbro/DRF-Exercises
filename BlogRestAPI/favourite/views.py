from rest_framework import serializers
from post.permissions import IsOwnerOrReadOnly
from favourite.paginations import FavPagination
from favourite.serializers import FavouriteDetailSerializer, FavouriteSerializer
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from favourite.models import Favourite

class FavouriteCreateListAPIView(ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    pagination_class = FavPagination
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class FavouriteDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializers = FavouriteDetailSerializer
    pagination_class =FavPagination
    permission_classes = [IsOwnerOrReadOnly]