from django.urls import path
from django.conf.urls import url

from .views import ( 
    StatusAPIView,
    StatusAPIDetailView 
    )

app_name = 'status'
urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('<pk>/', StatusAPIDetailView.as_view())
]