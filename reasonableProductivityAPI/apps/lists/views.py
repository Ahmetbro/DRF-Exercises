from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, status
from rest_framework.response import Response
from apps.lists.models import List, ListItem
from apps.lists.serializers import ListItemSerializer, ListSerializer

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

class ListItemAPIView(ListCreateAPIView):
    #queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

    def get_queryset(self):
        return ListItem.objects.filter(list_id = self.kwargs.get('id'))
    
    def perform_create(self, serializer):
        serializer.save(list_id = self.kwargs.get('id'))
    # def get(self, request, *args, **kwargs):
    #     item = ListItem.objects.filter(list_id = self.kwargs['id'])
    #     serializer = ListItemSerializer(item, many=True)
    #     return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     serializer = ListItemSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save(list_id=self.kwargs['id'])
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListItemDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ListItemSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return ListItem.objects.filter(list_id = self.kwargs.get('id'))
