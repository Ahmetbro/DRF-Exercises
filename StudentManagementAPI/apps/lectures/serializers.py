from django.db.models import fields
from .models import Lecture
from rest_framework import serializers


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'
