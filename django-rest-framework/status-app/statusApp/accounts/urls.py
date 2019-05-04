from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
# from django.conf.urls import url, include
from django.urls import path, include
from .views import AuthView, RegisterAPIView
# from user import views

app_name = 'accounts'
urlpatterns = [
    path('', AuthView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('auth/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token)
]