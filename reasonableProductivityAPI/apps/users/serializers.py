from django.db import models
from django.db.models import fields
from rest_framework import serializers
from apps.users.models import MyUser,UserProfile
from rest_framework.serializers import ModelSerializer



class UserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields= ('id','email', 'password')


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'
    
  