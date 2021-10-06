from django.shortcuts import render
from apps.task.serializers import TaskSerializer
from apps.task.models import Task
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer