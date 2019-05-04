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

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get_object(self):
    #     request = self.request
    #     passed_id = request.GET.get('id')
    #     queryset = self.get_queryset()
    #     obj = None
    #     if passed_id is not None:
    #         obj = get_object_or_404(queryset, id=passed_id)
    #         self.check_object_permissions(request, obj)
    #     return obj


# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []

#     def get(self, request, format=None):
#         query_set = Status.objects.all()
#         serializer = StatusSerializer(query_set, many=True)
#         return Response(serializer.data)

# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer

#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer