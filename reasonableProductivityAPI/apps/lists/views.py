from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from apps.lists.models import List
from apps.lists.serializers import ListSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



class ListAPIView(ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def get(self, request, *args, **kwargs):
        list = List.objects.filter(user_id = self.kwargs['pk'])
        serializer = ListSerializer(list, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=self.kwargs['pk'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ListDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = List.objects.filter(user_id = self.kwargs['pk']).get(id = self.kwargs['id'])
        serializer = ListSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)