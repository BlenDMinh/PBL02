from django.http import JsonResponse
from rest_framework.decorators import api_view

from UserManager.User import Student
from ClassManager.ClassSection import ClassSection
from ClassManager.Subject import Subject

import json

@api_view(['GET'])
def GetSubject(request, pk):
    return JsonResponse(Subject.GetByID(pk, AsDict=True), safe=False)

@api_view(['GET'])
def GetAllSubject(request):
    return JsonResponse(Subject.GetAll(AsDict=True), safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def Class(request, pk):
    if request.method == 'GET':
        return JsonResponse(ClassSection.GetByID(pk, AsDict=True), safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        if 'body' not in data and 'sid' not in data['body']:
            return JsonResponse({'error': 'argument "sid" not found!'})
        classSection = ClassSection.GetByID(pk)
        classSection.AddStudent(data['body']['sid'])  # type: ignore
        return JsonResponse({'status': 'OK', 'work': f'Added {request.POST.get("sid")} into {pk}'})
    
    elif request.method == 'DELETE':
        data = json.loads(request.body)
        if 'sid' not in data:
            return JsonResponse({'error': 'argument "sid" not found!'})
        classSection = ClassSection.GetByID(pk)
        classSection.RemoveStudent(data['sid'])  # type: ignore
        return JsonResponse({'status': 'OK', 'work': f'Removed {request.POST.get("sid")} from {pk}'}) 

@api_view(['GET'])
def GetAllClass(request):
    if 'sid' in request.GET:
        student : Student = Student.GetByID(request.GET.get('sid')) # type: ignore
        if 'mode' in request.GET:
            if request.GET.get('mode') == 'register':
                classes = ClassSection.GetAll()
                attended_classes = student.GetAttendedClasses()
                classList = []
                for classSection in classes:
                    if classSection not in attended_classes:
                        classList.append(classSection.AsDict()) # type: ignore
                return JsonResponse(classList, safe=False)
        else:
            return JsonResponse(student.GetAttendedClasses(AsDict=True), safe=False) #type: ignore
    return JsonResponse(ClassSection.GetAll(AsDict=True), safe=False)
