
from django.urls import path
from django.urls import re_path
from ClassManager import views

urlpatterns = [
    path("class", views.Debug)
]
