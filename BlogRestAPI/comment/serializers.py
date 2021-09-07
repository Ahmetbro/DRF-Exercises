from django.db.models import fields
from comment.models import Comment
from rest_framework import serializers


# class CommentChildSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'

    def validate(self, attrs):
        if(attrs["parent"]):
            if attrs["parent"].post != attrs["post"]:
                raise serializers.ValidationError("select correct post/parent")
    
    def get_replies(self, obj):
        if obj.any_children:
            return CommentSerializer(obj.children(), many=True).data


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']