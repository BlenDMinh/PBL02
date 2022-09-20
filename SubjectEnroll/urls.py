from django.urls import re_path
from SubjectEnroll import views 

urlpatterns = [ 
    re_path(r'^api/SubjectEnrolls$', views.SubjectEnroll_list),
    re_path(r'^api/SubjectEnrolls/(?P<pk>[0-9]+)$', views.SubjectEnroll_detail),
    re_path(r'^api/SubjectEnrolls/published$', views.SubjectEnroll_list_published)
]