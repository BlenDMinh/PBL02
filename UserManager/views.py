from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from UserManager.Student import Student
from UserManager.User import User

# Create your views here.

# @api_view(['GET', 'POST', 'DELETE'])
# def Debug(request):
#     anhminh = Student('102210040', 'Nguyễn Trương Anh Minh', Sex.MALE, '0769639972', '01/12/2003', '21TCLC_Nhat1')
#     print(anhminh.GetClassName())
#     print(anhminh.__dict__)
#     return JsonResponse(anhminh.__dict__, safe=False)

@api_view(['GET'])
def GetStudent(request, pk: str):
    student = Student.GetStudentFromDatabase(pk=pk, AsDict=True)
    return JsonResponse(student, safe=False)

def GetStudentList(request):
    studentList = Student.GetAllStudentFromDatabase(AsDict=True)
    return JsonResponse(studentList, safe=False)

# return a token if valid
@api_view(['GET'])
def UserLogin(request):
    if request.method == 'GET':
        print(request.GET)
        if 'id' in request.GET and 'password' in request.GET:
            id = request.GET.get('id')
            password = request.GET.get('password')
            data = User.Authenticate(id=id, password=password)
            if not data:
                return JsonResponse({'error': 'User ID is not valid or password is wrong'})
            
            return JsonResponse({'token': data})
        
        if 'token' in request.GET:
            token = request.GET.get('token')
            data = User.TokenAuthenticate(token)
            print(data)
            if not data:
                return JsonResponse({'error': 'User ID is not valid or password is wrong'})
            
            return JsonResponse(data)

@api_view(['DELETE'])
def UserLogout(request, token):
    User.TokenLogout(token=token)
    return JsonResponse({'status': f'Removed {token}'})