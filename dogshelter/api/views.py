from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, status
from rest_framework.response import Response
from api.serializers import DogSerializer, BreedSerializer
from rest_framework.views import APIView
from api.models import Dog, Breed
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin,RetrieveModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class DogList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        dog = Dog.objects.all()
        serializer = DogSerializer(dog, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Bad Data', status=status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, pk=None):
        dog = get_object_or_404(Dog, pk=pk)
        return dog
    
    def get(self, request, pk=None):
        dog = Dog.objects.get(pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk=None):
        dog = self.get_object()
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        dog = self.get_object()
        dog.delete()
        return Response('Deleted', status=status.HTTP_204_NO_CONTENT)

class BreedList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class BreedDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

