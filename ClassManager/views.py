from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from ClassManager.ClassSection import ClassSection
from ClassManager.Subject import Subject

def Debug(request):
    return JsonResponse(ClassSection.GetAllClasses(AsDict=True), safe=False)

@api_view(['GET'])
def GetSubject(request, pk):
    return JsonResponse(Subject.GetSubjectByID(pk, AsDict=True), safe=False)

@api_view(['GET'])
def GetAllSubject(request):
    return JsonResponse({"error": "not available"}, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def GetClass(request, pk):
    return JsonResponse(ClassSection.GetClassByID(pk, AsDict=True), safe=False)

@api_view(['GET'])
def GetAllClass(request):
    return JsonResponse(ClassSection.GetAllClasses(AsDict=True), safe=False)