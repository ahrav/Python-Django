from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'^register$', views.register),
url(r'^login$', views.login),
url(r'^travels$', views.dashboard),
url(r'^travels/add', views.add),
url(r'add_plan$', views.add_plan),
url(r'join/(?P<trip_id>\d+)', views.join_trip),
url(r'^travels/destination/(?P<trip_id>\d+)$', views.show_destination),
url(r'logout$', views.logout)
]
