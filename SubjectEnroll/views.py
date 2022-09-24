from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

import SubjectEnroll
from SubjectEnroll.models import TestData

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def SubjectEnroll_list(request):
    print(request.data)
    return JsonResponse({'message': 'The TestData yeah'}, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def SubjectEnroll_detail(request, pk):
    try: 
        testData = SubjectEnroll.objects.get(pk=pk) 
    except SubjectEnroll.DoesNotExist: 
        return JsonResponse({'message': 'The TestData does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['GET'])
def SubjectEnroll_list_published(request):
    return JsonResponse({'message': 'The TestData yeah'}, status=status.HTTP_200_OK)