from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.urls import path, include
from .views import AuthView, RegisterAPIView
# from user import views

app_name = 'accounts'
urlpatterns = [
    path('', AuthView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('auth/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token)
]