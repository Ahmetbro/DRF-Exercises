from django.db.models import fields
from django.utils import tree
from rest_framework import serializers
from haberler.models import Makale, Gazeteci
from rest_framework.validators import ValidationError



class MakaleSerializer(serializers.ModelSerializer):
    # yazar = serializers.StringRelatedField()
    # yazar = GazeteciSerializer(many=True, read_only=True)
    class Meta:
        model = Makale
        fields = '__all__'


class GazeteciSerializer(serializers.ModelSerializer):
    # makaleler = MakaleSerializer(many=True, read_only=True)
    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detay'
    )

    class Meta:
        model = Gazeteci
        fields = '__all__'








# class MakaleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     yazar = serializers.CharField()
#     baslik = serializers.CharField()
#     aciklama = serializers.CharField()
#     metin = serializers.CharField()
#     sehir = serializers.CharField()
#     yayin_tarihi = serializers.DateField()
#     aktif = serializers.BooleanField(default=True)
#     yaratilma_tarihi = serializers.DateTimeField(read_only=True)
#     guncellenme_tarihi = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return Makale.objects.create(**validated_data)

#     def update(self, instance ,validated_data):
#         instance.yazar = validated_data.get('yazar', instance.yazar)
#         instance.baslik = validated_data.get('baslik', instance.baslik)
#         instance.aciklama = validated_data.get('aciklama', instance.aciklama)
#         instance.metin = validated_data.get('metin', instance.metin)
#         instance.sehir = validated_data.get('sehir', instance.sehir)
#         instance.yayin_tarihi = validated_data.get('yayin_tarihi', instance.yayin_tarihi)
#         instance.aktif = validated_data.get('aktif', instance.aktif)
#         instance.save()
#         return instance
