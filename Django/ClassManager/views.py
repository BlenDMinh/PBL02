from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from ClassManager.ClassSection import ClassSection
from ClassManager.Subject import Subject

@api_view(['GET'])
def GetSubject(request, pk):
    return JsonResponse(Subject.GetByIDFromDatabase(pk, AsDict=True), safe=False)

@api_view(['GET'])
def GetAllSubject(request):
    return JsonResponse(Subject.GetAllFromDatabase(AsDict=True), safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def Class(request, pk):
    if request.method == 'GET':
        return JsonResponse(ClassSection.GetByIDFromDatabase(pk, AsDict=True), safe=False)
    
    elif request.method == 'POST':
        if not request.POST.get("sid"):
            return JsonResponse({'error': 'argument "sid" not found!'})
        classSection = ClassSection.GetByIDFromDatabase(pk)
        classSection.AddStudent(request.POST.get("sid"))  # type: ignore
        return JsonResponse({'status': 'OK', 'work': f'Added {request.POST.get("sid")} into {pk}'})
    
    elif request.method == 'DELETE':
        if not request.POST.get("sid"):
            return JsonResponse({'error': 'argument "sid" not found!'})
        classSection = ClassSection.GetByIDFromDatabase(pk)
        classSection.RemoveStudent(request.POST.get("sid"))  # type: ignore
        return JsonResponse({'status': 'OK', 'work': f'Removed {request.POST.get("sid")} from {pk}'})
    

@api_view(['GET'])
def GetAllClass(request):
    if 'sid' in request.GET:
        return JsonResponse(ClassSection.GetClassesAttendedByID(request.GET.get('sid'), AsDict=True), safe=False)
    return JsonResponse(ClassSection.GetAllFromDatabase(AsDict=True), safe=False)