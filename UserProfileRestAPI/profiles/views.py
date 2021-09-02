from django.shortcuts import render
from rest_framework import generics
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from profiles.models import Profile, ProfilStatus
from profiles.serializers import ProfilesSerializer, ProfilePhotoSerializer, ProfileStatusSerializer
from profiles.permissions import IsOwnProfileOrReadOnly

# Create your views here.

class ProfileViewset(
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                GenericViewSet
                ):

    queryset=Profile.objects.all()
    serializer_class= ProfilesSerializer
    permission_classes = [IsOwnProfileOrReadOnly]
