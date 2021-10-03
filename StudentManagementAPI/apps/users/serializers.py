from apps.users.models import User
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'password', 'is_student']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 10}}

    def create(self, validated_data):
        return User.objects.create(**validated_data)