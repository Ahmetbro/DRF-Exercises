from django.db.models import fields
from post.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    class Meta:
        model = Post
        exclude = ['user']