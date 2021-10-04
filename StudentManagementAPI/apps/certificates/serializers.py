from django.db.models import fields
from .models import Certificate
from rest_framework import serializers


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'
