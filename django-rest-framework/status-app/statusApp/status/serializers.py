from rest_framework import serializers
from accounts.serializers import UserSerializer

from .models import Status

class StatusInlineuserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'uri'
        ]
    
    def get_uri(self, obj):
        return '/api/status/{id}'.format(id=obj.id)

class StatusSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'uri'
        ]
        read_only_fields = ['user']
    
    def get_uri(self, obj):
        return '/api/status/{id}'.format(id=obj.id)

    # Field level validation
    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError('This is way too long')
    #     return value

    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError('Content or image is required')
        return data