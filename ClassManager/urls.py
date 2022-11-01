
from django.urls import path
from django.urls import re_path
from ClassManager import views

urlpatterns = [
    path("api/subject", views.GetAllSubject),
    re_path(r'api/subject/(?P<pk>[0-9]+)$', views.GetSubject),
    path("api/class", views.Debug),
    path("api/classsection", views.GetAllClass),
    re_path(r'api/classsection/(?P<pk>[0-9]+)$', views.GetClass),
]
