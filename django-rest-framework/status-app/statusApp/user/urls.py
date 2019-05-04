# from django.conf.urls import url, include
from django.urls import path
from .views import UserDetailAPIView, UserStatusAPIView

app_name = 'user'
urlpatterns = [
    path('', UserDetailAPIView.as_view(), name="detail"),
    path('status/', UserStatusAPIView.as_view(), name="status-list"),
]