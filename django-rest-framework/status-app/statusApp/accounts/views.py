from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserRegisterSerializer 
from user.serializers import UserDetailSerializer
from .permissions import AnonPermissionOnly

from .utils import jwt_response_payload_handler

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()


# Create your views here.
class AuthView(APIView):
    permission_classes = [AnonPermissionOnly]
    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        qs = User.objects.filter(
            Q(username__iexact=username)|
            Q(email__iexact=username)
        ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user, request=request)
                return Response(response)
        return Response({"detail": "Invalid credentials"}, status=401)

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AnonPermissionOnly]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}