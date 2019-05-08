from rest_framework import serializers
from accounts.serializers import UserSerializer
from rest_framework.reverse import reverse as api_reverse

from .models import Status

class StatusSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)
    user_id = serializers.HyperlinkedRelatedField(
        source='user',
        lookup_field='username',
        view_name='user:detail',
        read_only=True
    )
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    # user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id',
            'user_id',
            'user',
            'content',
            'image',
            'uri'
        ]
        read_only_fields = ['user']
    
    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("status:detail", kwargs={'id': obj.id}, request=request)

    # def get_user(self, obj):
    #     request = self.context.get('request')
    #     user = obj.user
    #     return UserSerializer(user, read_only=True, context={'request': request}).data

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
        request = self.context.get('request')
        return api_reverse('status:detail', kwargs={"id": obj.id}, request=request)