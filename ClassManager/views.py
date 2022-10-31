from django.http import JsonResponse
from django.shortcuts import render

from ClassManager.ClassSection import ClassSection

def Debug(request):
    return JsonResponse(ClassSection.GetClassByID('1', AsDict=True), safe=False)
