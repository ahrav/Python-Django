import datetime
from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth import get_user_model

from status.serializers import StatusInlineuserSerializer

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status',
        ]
    
    def get_uri(self, obj):
        return '/api/users/{id}'.format(id=obj.id)

    def get_status(self, obj):
        qs = obj.status_set.all().order_by("-timestamp") #Status.objects.filter(user=obj)
        data = {
            'uri' : self.get_uri(obj) + 'status/',
            'last': StatusInlineuserSerializer(qs.first()).data,
            'recent': StatusInlineuserSerializer(qs[:10], many=True).data
        }
        return data