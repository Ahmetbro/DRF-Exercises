from django.shortcuts import get_object_or_404, render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from apps.task import serializers
from apps.task.serializers import TaskSerializer
from apps.task.models import Task
from rest_framework import viewsets, status
from rest_framework.response import Response

class TaskView(APIView):
    def get(self, request, format=None, **kwargs):
        task = Task.objects.filter(user_id=self.kwargs['pk'])
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response  (serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = Task.objects.filter(user_id = self.kwargs['pk'])
        serializer = TaskSerializer(instance)
