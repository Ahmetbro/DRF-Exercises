from django.db.models import fields
from post.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    username = serializers.SerializerMethodField(method_name='new_username')
    class Meta:
        model = Post
        exclude = ['user']  # post ederken user seçmemize gerek yok fakat list ederken username i görmek istiyoruz

    def new_username(self, obj):
        return str(obj.user.username)    