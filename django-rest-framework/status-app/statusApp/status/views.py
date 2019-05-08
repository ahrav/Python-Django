from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import StatusSerializer
from .models import Status
from accounts.permissions import IsOwnerOrReadOnly


class StatusAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     serializer.save(updated_by_user=self.request.user)
    
    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None

class StatusAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    search_fields = ('user__username', 'content')
    ordering_fields = ('user__username', 'timestamp')
    queryset = Status.objects.all()
    lookup_field = 'id'

    # def get_queryset(self):
    #     qs = Status.objects.all()
    #     query = self.request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(content__icontains=query)
    #     return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
