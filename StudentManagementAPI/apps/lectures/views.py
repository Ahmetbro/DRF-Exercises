from apps.lectures.serializers import LectureSerializer
from django.shortcuts import render



from .models import Lecture
from rest_framework import viewsets


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer