from django.urls import path
from django.urls import re_path
from UserManager import views

urlpatterns = [
    path('api/user/student/', views.GetStudentList),
    path('api/user/student', views.GetStudentList),
    re_path(r'api/user/student/(?P<pk>[0-9]+)$', views.GetStudent),
    path('api/user/teacher/', views.GetTeacherList),
    re_path(r'api/user/teacher/(?P<pk>[0-9]+)$', views.GetTeacher),
    re_path(r'api/user/login', views.UserLogin),
    re_path(r'api/user/logout/(?P<token>(\D|\d)+)$', views.UserLogout)
]
