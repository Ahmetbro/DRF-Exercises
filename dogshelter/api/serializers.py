from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from api.models import Dog, Breed
from rest_framework import serializers


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):
<<<<<<< Updated upstream
    # breed = serializers.StringRelatedField(read_only=True)
    dropped_by = serializers.SerializerMethodField()
=======
    #breed = serializers.StringRelatedField(read_only=True)
>>>>>>> Stashed changes
    class Meta:
        model = Dog
        exclude = ('ex_owner',)

    def get_dropped_by(self, obj):
        return str(obj.ex_owner.username)
