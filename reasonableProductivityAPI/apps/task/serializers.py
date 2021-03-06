from django.db.models import fields
from rest_framework import serializers
from .models import Tag, Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Task
        fields = '__all__'
    
    



