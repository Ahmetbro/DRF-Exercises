from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile, ProfilStatus
from profiles.serializers import ProfilesSerializer, ProfilePhotoSerializer, ProfileStatusSerializer

# Create your views here.

class ProfileList(generics.ListAPIView):
    queryset=Profile.objects.all()
    serializer_class= ProfilesSerializer
    permission_classes = [IsAuthenticated]
