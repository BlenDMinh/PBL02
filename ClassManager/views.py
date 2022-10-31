from django.http import JsonResponse
from django.shortcuts import render

from ClassManager.ClassSection import ClassSection

def Debug(request):
    return JsonResponse(ClassSection.GetAllClasses(AsDict=True), safe=False)
