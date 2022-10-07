from django.urls import path
from django.urls import re_path
from UserManager import views

urlpatterns = [
    path('api/user/student/', views.GetStudentList),
    re_path(r'api/user/student/(?P<pk>[0-9]+)$', views.GetStudent)
]