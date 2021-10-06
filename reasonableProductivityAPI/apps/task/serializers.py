from django.db.models import fields
from rest_framework import serializers
from .models import Tag, Task

class TaskSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Task
        exclude = ('user',)
    
    def get_username(self, obj):
        return str(obj.user.email)


class TagSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True, many=True)

    class Meta:
        model=Tag
        fields = ('text','task')

