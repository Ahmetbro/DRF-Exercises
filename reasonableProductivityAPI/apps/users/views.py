from rest_framework import serializers
from rest_framework.response import Response
from apps.users.serializers import UserProfileSerializer, UserSerializer
from apps.users.models import MyUser, UserProfile
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView


class UserCreateAPIView(ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class UserProfileCreateListAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = UserProfile.objects.filter(user_id = self.kwargs['pk'])
        serializer = UserProfileSerializer(instance, many=True)
        return Response(serializer.data)
    # def list(self, request, *args, **kwargs):
    #     queryset = UserProfile.objects.filter(user_id = self.kwargs['pk'])
    #     serializer = UserProfileSerializer(queryset, many=True)
    #     return Response(serializer.data)
