from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserDetailSerializer
from status.serializers import StatusInlineuserSerializer
from status.models import Status

User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

class UserStatusAPIView(generics.ListAPIView):
    serializer_class = StatusInlineuserSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get('username', None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)