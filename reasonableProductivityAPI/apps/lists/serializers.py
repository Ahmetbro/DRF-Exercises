from django.db.models import fields
from rest_framework import serializers
from apps.lists.models import List


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