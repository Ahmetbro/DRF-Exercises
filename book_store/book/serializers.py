import book
from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from book.models import Book, Comment
from rest_framework.validators import ValidationError



class CommentSerializer(serializers.ModelSerializer):
    comment_owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['book']

class BookSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = '__all__'
