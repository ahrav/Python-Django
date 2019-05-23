from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.urls import path, include

from .views import LoginAPIView, RegisterAPIView

app_name = 'users'
urlpatterns = [
    # path('', LoginAPIView.as_view(), name='login'),
    # path('register/', RegisterAPIView.as_view(), name='register'),
    # path('<username>/', UserDetailAPIView.as_view(), name="detail"),
    # path('<username>/status/', UserStatusAPIView.as_view(), name="status-list"),
    # path('auth/', obtain_jwt_token),
    # path('refresh/', refresh_jwt_token)
]