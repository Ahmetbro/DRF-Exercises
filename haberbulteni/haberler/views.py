from django.http import request
from django.shortcuts import render
from rest_framework import serializers, status, generics
from haberler.serializers import GazeteciSerializer, MakaleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from haberler.models import Gazeteci, Makale
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
# Create your views here.

##### generics
class MakaleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Makale.objects.all()
    serializer_class = MakaleSerializer

class MakaleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Makale.objects.all()
    serializer_class = MakaleSerializer

class GazeteciListCreateAPIView(generics.ListCreateAPIView):
    queryset = Gazeteci.objects.all()
    serializer_class = GazeteciSerializer

class GazeteciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gazeteci.objects.all()
    serializer_class = GazeteciSerializer


###### GENERIC API VIEWS ##########
# class MakaleListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Makale.objects.all()
#     serializer_class = MakaleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# class GazeteciListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Gazeteci.objects.all()
#     serializer_class = GazeteciSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# ###### WITH CLASS VIEWS ###########
# class GazeteciListCreateAPIView(APIView):
#     def get(self, request):
#         gazeteci = Gazeteci.objects.all()
#         serializer = GazeteciSerializer(gazeteci, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = GazeteciSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# class GazeteciDetailAPIView(APIView):
#     def get_object(self, pk=None):
#         gazeteci = get_object_or_404(Gazeteci, pk=pk)
#         return gazeteci
    
#     def get(self, request, pk=None):
#         gazeteci = self.get_object()
#         serializer = GazeteciSerializer(gazeteci)
#         return Response(serializer.data)

#     def put(self, request, pk=None):
#         gazeteci = self.get_object()
#         serializer = GazeteciSerializer(gazeteci, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk=None):
#         gazeteci = self.get_object()
#         gazeteci.delete()
#         return Response('Silindi', status=status.HTTP_204_NO_CONTENT)

# class MakaleListCreateAPIView(APIView):
#     def get(self, request):
#         makaleler = Makale.objects.filter(aktif=True)
#         serializer = MakaleSerializer(makaleler, many=True)
#         return Response(serializer.data) 

#     def post(self, request):
#         serializer = MakaleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)



# class MakaleDetailAPIView(APIView):
#     def get_object(self, pk=None):
#         makale_instance = get_object_or_404(Makale, pk=pk)
#         return makale_instance

#     def get(self, request, pk=None):
#         makale = self.get_object(pk=pk)
#         serializer = MakaleSerializer(makale)
#         return Response(serializer.data)

#     def put(self, request, pk=None):
#         makale = self.get_object(pk=pk)
#         serializer = MakaleSerializer(makale, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request, pk=None):
#         makale = self.get_object(pk=pk)
#         makale.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ######## WITH DECORATORS ###########

# @api_view(['GET', 'POST'])
# def makale_list_create_api_view(request):
    
#     if request.method == 'GET':
#         makaleler = Makale.objects.filter(aktif = True)
#         serializer = MakaleSerializer(makaleler, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = MakaleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def makale_detail_api_view(request, pk):
#     try:
#         makale_instance = Makale.objects.get(pk=pk)
#     except Makale.DoesNotExist:
#         return Response(
#             {
#                 'errors': {
#                     'code': 404,
#                     'message': 'böyle bir makale bulunamadi'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#             )
#     if request.method == 'GET':
#         serializers = MakaleSerializer(makale_instance)
#         return Response(serializers.data)

#     elif request.method == 'PUT':
#         serializer = MakaleSerializer(makale_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         makale_instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)








