from django.shortcuts import render

from apps.certificates.serializers import CertificateSerializer

from .models import Certificate
from rest_framework import viewsets


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer