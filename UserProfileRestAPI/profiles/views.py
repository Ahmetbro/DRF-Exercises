from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from profiles.models import Profile, ProfilStatus
from profiles.serializers import ProfilesSerializer, ProfilePhotoSerializer, ProfileStatusSerializer
from profiles.permissions import IsOwnProfileOrReadOnly, IsOwnStatusOrReadOnly
from rest_framework.filters import SearchFilter

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
    filter_backends = [SearchFilter]
    search_fields = ['city']             # ?search={city}

class ProfileStatusViewset(ModelViewSet):
    queryset = ProfilStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated,IsOwnStatusOrReadOnly]

    def get_queryset(self):
        queryset = ProfilStatus.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username) # profil status modelimdeki profil user a bağllı user ın username ini çekip karşılaştırdık
            return queryset

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)


class ProfilePhotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilePhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile = self.request.user.profile
        return profile


