from django.urls import path

from .views import ( 
    WorkoutAPIView,
    WorkoutAPIDetailView 
    )

app_name = 'workouts'
urlpatterns = [
    path('', WorkoutAPIView.as_view(), name='list'),
    path('<id>/', WorkoutAPIDetailView.as_view(), name='detail')
]