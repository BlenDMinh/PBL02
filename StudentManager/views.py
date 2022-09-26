from enum import Flag
import json
import csv
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from StudentManager.Student import Student
from StudentManager.User import Sex

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def Debug(request):
    anhminh = Student('102210040', 'Nguyễn Trương Anh Minh', Sex.MALE, '0769639972', '01/12/2003', '21TCLC_Nhat1')
    print(anhminh.GetClassName())
    print(anhminh.__dict__)
    return JsonResponse(anhminh.__dict__, safe=False)

@api_view(['GET'])
def GetStudentList(request):
    studentList = []
    with open('./assets/21TCLC_Nhat1.csv', encoding="UTF-8") as file:
        data = csv.reader(file, delimiter=',', quotechar='|')
        for row in data:
            studentList.append(Student(row[1], row[2], Sex.MALE, row[4], '', row[3]).AsDist())
    return JsonResponse(studentList, safe=False)
    # return JsonResponse(json.dumps(studentList, ensure_ascii=False, default=vars), safe=False)