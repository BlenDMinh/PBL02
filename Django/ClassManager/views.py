from django.http import JsonResponse
from rest_framework.decorators import api_view

from UserManager.User import Student
from ClassManager.ClassSection import ClassSection
from ClassManager.Subject import Subject

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
        if not request.POST.get("sid"):
            return JsonResponse({'error': 'argument "sid" not found!'})
        classSection = ClassSection.GetByID(pk)
        classSection.AddStudent(request.POST.get("sid"))  # type: ignore
        return JsonResponse({'status': 'OK', 'work': f'Added {request.POST.get("sid")} into {pk}'})
    
    elif request.method == 'DELETE':
        if not request.POST.get("sid"):
            return JsonResponse({'error': 'argument "sid" not found!'})
        classSection = ClassSection.GetByID(pk)
        classSection.RemoveStudent(request.POST.get("sid"))  # type: ignore
        return JsonResponse({'status': 'OK', 'work': f'Removed {request.POST.get("sid")} from {pk}'}) 

@api_view(['GET'])
def GetAllClass(request):
    if 'sid' in request.GET:
        student = Student.GetByID(request.GET.get('sid'))
        return JsonResponse(student.GetAttendedClasses(AsDict=True), safe=False) #type: ignore
    
    return JsonResponse(ClassSection.GetAll(AsDict=True), safe=False)
