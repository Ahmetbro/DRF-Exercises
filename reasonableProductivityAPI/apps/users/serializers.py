from django.db import models
from django.db.models import fields
from rest_framework import serializers
from apps.users.models import MyUser,UserProfile
from rest_framework.serializers import ModelSerializer



class UserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields= ('id','email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data)

class UserProfileSerializer(ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'
    
  