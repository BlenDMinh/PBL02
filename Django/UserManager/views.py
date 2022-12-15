from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views import View

from UserManager.User import Student
from UserManager.User import Teacher
from UserManager.User import User

class StudentView(View):
    pass

# Create your views here.
@api_view(['GET'])
def GetStudent(request, pk: str):
    student = Student.GetByID(id=pk, AsDict=True)
    return JsonResponse(student, safe=False)

@api_view(['GET'])
def GetStudentList(request):
    studentList = Student.GetAll(AsDict=True)
    return JsonResponse(studentList, safe=False)

@api_view(['GET'])
def GetAttendedClassOfStudent(request, pk: str):
    student = Student.GetByID(id=pk)
    return JsonResponse(student.GetAttendedClasses(AsDict=True), safe=False) # type: ignore

@api_view(['GET'])
def GetTeacher(request, pk: str):
    teacher = Teacher.GetByID(id=pk, AsDict=True)
    return JsonResponse(teacher, safe=False)

@api_view(['GET'])
def GetTeacherList(request):
    teacherList = Teacher.GetAll(AsDict=True)
    return JsonResponse(teacherList, safe=False)

# return a token if valid
@api_view(['GET'])
def UserLogin(request):
    if request.method == 'GET':
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