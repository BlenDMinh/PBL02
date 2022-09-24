import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from StudentManager.Student import Student
from StudentManager.User import Sex

# Create your views here.
def Debug(request):
    anhminh = Student('102210040', 'Nguyễn Trương Anh Minh', Sex.MALE, '0769639972', '01/12/2003', '21TCLC_Nhat1')
    print(anhminh.GetClassName())
    print(anhminh.__dict__)
    return JsonResponse(anhminh.__dict__, safe=False)