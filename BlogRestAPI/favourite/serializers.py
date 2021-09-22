from django.db.models import fields
from favourite.models import Favourite
from rest_framework import serializers

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'


    def validate(self, attrs):
        queryset = Favourite.objects.filter(post = attrs['post'], user = attrs['user'])
        if queryset.exists():
            raise serializers.ValidationError('Post already added to favourites')
        return attrs
    

class FavouriteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ['content']
    
