from mimetypes import init
from enum import IntEnum
import hashlib
from datetime import datetime
from Interface import IObject
from Database.TokenDatabase import TokenDatabase
from Database.StudentDatabase import StudentDatabase
from Database.TeacherDatabase import TeacherDatabase

class Sex(IntEnum):
    MALE = 0
    FEMALE = 1
    OTHER = 2

class User:
    def __init__(self, userid='', name='', sex=Sex.OTHER, phone_number='', birthday=''):
        self.__userid = userid
        self.__name = name
        self.__sex = sex
        self.__phone_number = phone_number
        self.__birthday = birthday
        
    def GetUserID(self):
        return self.__userid
    
    def GetUserName(self):
        return self.__name
    
    def GetUserSex(self):
        return self.__sex
    
    def GetUserPhoneNumber(self):
        return self.__phone_number
    
    def GetUserBirthday(self):
        return self.__birthday
    
    @staticmethod
    def Authenticate(id, password):
        if not StudentDatabase.Login(id, password):
            return ''
        
        # if anthentication pass
        dummy = hashlib.md5((id + password + datetime.now().strftime('%m/%d/%Y-%H:%M:%S')).encode('utf-8')).hexdigest()
        dummy1 = hashlib.sha256(dummy.encode('utf-8')).hexdigest()
        token = hashlib.sha512(dummy1.encode('utf-8')).hexdigest()
        TokenDatabase.Insert({'token': token, 'userid': id})
        return token
    
    @staticmethod
    def TokenAuthenticate(token):
        UserID = TokenDatabase.Get(token)
        if UserID != None:
            return Student.GetByIDFromDatabase(UserID, AsDict=True)  # type: ignore
        return ''

    @staticmethod
    def TokenLogout(token):
        TokenDatabase.Delete(token)

class Student(User, IObject):
    
    __classname: str
    
    def __init__(self, userid, name, sex, phone_number, birthday, classname) -> None:  # type: ignore
        super().__init__(userid, name, sex, phone_number, birthday)
        self.__classname = classname
    
    def __str__(self):
        str = f'{self.GetUserID()} {self.GetUserName()} {self.GetUserSex()} {self.GetClassName()}'
        return str
    
    def AsDict(self):
        return {
            'studentId': self.GetUserID(),
            'name': self.GetUserName(),
            'sex': self.GetUserSex(),
            'class': self.GetClassName(),
            'phoneNumber': self.GetUserPhoneNumber(),
            'birthday': self.GetUserBirthday()
        }
    
    def GetClassName(self):
        return self.__classname

    @staticmethod
    def FromRecord(record, AsDict=False):
        student = Student(record[0], record[1], record[2], record[4], record[5], record[3])
        if AsDict:
            return student.AsDict()
        return student

    @staticmethod
    def GetAllFromDatabase(AsDict = False):
        students_database = StudentDatabase.GetAll()
        studentList = []
        for rec in students_database:
            studentList.append(Student.FromRecord(record=rec, AsDict=AsDict))
        return studentList
    
    @staticmethod
    def GetByIDFromDatabase(id, AsDict = False):
        rec = StudentDatabase.Get(id)
        student = Student.FromRecord(record=rec, AsDict=AsDict)
        return student
    
    def GetAttendedClasses(self, AsDict = False):
        pass
    
class Teacher(User, IObject):
    
    def __init__(self, userid, name, sex, phone_number, birthday):  # type: ignore
        super().__init__(userid, name, sex, phone_number, birthday)
    
    def AsDict(self):
        return {
            'teacherId': self.GetUserID(),
            'name': self.GetUserName(),
            'sex': self.GetUserSex(),
            'phoneNumber': self.GetUserPhoneNumber(),
            'birthday': self.GetUserBirthday()
        }
    
    @staticmethod
    def FromRecord(record, AsDict=False):
        teacher = Teacher(record[0], record[1], record[2], record[3], record[4])
        if AsDict:
            return teacher.AsDict()
        return teacher

    @staticmethod
    def GetByIDFromDatabase(id, AsDict = False):
        rec = TeacherDatabase.Get(id)
        teacher = Teacher.FromRecord(record=rec, AsDict=AsDict)
        return teacher
        
    @staticmethod
    def GetAllFromDatabase(AsDict = False):
        teachers_database = TeacherDatabase.GetAll()
        teacherList = []
        for rec in teachers_database:
            if AsDict:
                teacherList.append(Teacher.FromRecord(rec, AsDict=AsDict))
        return teacherList
