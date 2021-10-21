from django.db import models
from django.db.models import fields
from rest_framework import serializers
from apps.lists.models import List, ListItem


class ListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = List
        fields = (
            "id",
            "user",
            "name",
            "created_at",
            "updated_at",
        )
class ListItemSerializer(serializers.ModelSerializer):
    list = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ListItem
        fields = (
            'id',
            'list',
            'text',
            'slug',
            'created_at',
            'updated_at',
        )

   