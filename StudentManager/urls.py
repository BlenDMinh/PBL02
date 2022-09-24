from django.urls import path
from StudentManager import views

urlpatterns = [
    path('api/StudentManager', views.GetStudentList),
]