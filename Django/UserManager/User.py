from enum import IntEnum
import hashlib
from datetime import datetime
from Interface import IObject
from Exception import RecordException

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
        
    def GetUserID(self) -> str:
        return self.__userid
    
    def GetUserName(self) -> str:
        return self.__name
    
    def GetUserSex(self) -> Sex:
        return self.__sex
    
    def GetUserPhoneNumber(self) -> str:
        return self.__phone_number
    
    def GetUserBirthday(self) -> str:
        return self.__birthday
    
    def SetUserName(self, name: str) -> None:
        self.__name = name
        
    def SetUserSex(self, sex: Sex) -> None:
        self.__sex = sex
    
    def SetUserPhoneNumber(self, phone_number : str) -> None:
        self.__phone_number = phone_number
    
    def SetUserBirthday(self, birthday : str) -> None:
        self.__birthday = birthday
    
    @staticmethod
    def Authenticate(id, password) -> str:
        from Database.TokenDatabase import TokenDatabase
        from Database.StudentDatabase import StudentDatabase
        
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
        from Database.TokenDatabase import TokenDatabase
        
        UserID = TokenDatabase.Get(token)
        if UserID != None:
            return Student.GetByID(UserID, AsDict=True)  # type: ignore
        return None

    @staticmethod
    def TokenLogout(token):
        from Database.TokenDatabase import TokenDatabase
        
        TokenDatabase.Delete(token)

class Student(User, IObject):
    
    def __init__(self, userid : str, name : str, sex : Sex, phone_number : str, birthday : str, classname : str, attendedClassSections = []) -> None:  # type: ignore
        super().__init__(userid, name, sex, phone_number, birthday)
        self.__classname = classname
        self.__attendedClassSections = attendedClassSections
    
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
        
    def GetPrimaryKey(self) -> str:
        return self.__userid
    
    def GetClassName(self) -> str:
        return self.__classname
    
    def SetClassName(self, classname : str) -> None:
        self.__classname = classname

    def GetAttendedClasses(self, AsDict = False):
        from Database.StudentDatabase import StudentDatabase
        
        if not StudentDatabase.IsClassesLoaded(self.GetUserID()):
            StudentDatabase.FetchFromDatabase(self.GetUserID())
        if not AsDict:
            return self.__attendedClassSections
        retList = []
        for classSection in self.__attendedClassSections:
            retList.append(classSection.AsDict())
        return retList
    
    def _SetAttenedClasses(self, classes: list):
        self.__attendedClassSections = classes
        
    def _AddClassSection(self, classSection):
        from Database.StudentDatabase import StudentDatabase
        if StudentDatabase.IsClassesLoaded(self.GetUserID()):
            StudentDatabase.FetchFromDatabase(self.GetUserID())
        self.__attendedClassSections.append(classSection)
        
    def _RemoveClassSection(self, classSection):
        from Database.StudentDatabase import StudentDatabase
        if StudentDatabase.IsClassesLoaded(self.GetUserID()):
            StudentDatabase.FetchFromDatabase(self.GetUserID())
        if classSection in self.__attendedClassSections:
            self.__attendedClassSections.remove(classSection)

    @staticmethod
    def FromRecord(record) -> 'Student':
        for i in range(len(record)):
            ele = record[i]
            if ele == None:
                raise RecordException(f"Element {i} of Student record is None or Empty")
        
        from Database.ClassSectionDatabase import ClassSectionDatabase
        classList = []
        try:
            for pk in record[6]:
                ClassSectionDatabase.FetchFromDatabase(pk[0], True)
                classList.append(ClassSectionDatabase.Get(pk[0]))
        except IndexError:
            pass
        student = Student(record[0], record[1], record[2], record[4], record[5], record[3], classList)
        
        return student

    @staticmethod
    def GetAll(AsDict = False):
        from Database.StudentDatabase import StudentDatabase
        students = StudentDatabase.GetAll()
        if AsDict:
            return list([student.AsDict() for student in students])
        return students

    
    @staticmethod
    def GetByID(id, AsDict = False):
        from Database.StudentDatabase import StudentDatabase
        student = StudentDatabase.Get(id)
        if AsDict:
            return student.AsDict()
        return student
    
    
class Teacher(User, IObject):
    
    __teachingClassSections = []
    
    def __init__(self, userid : str, name : str, sex : Sex, phone_number : str, birthday : str, teachingClassSections = []):  # type: ignore
        super().__init__(userid, name, sex, phone_number, birthday)
        self.__teachingClassSections = teachingClassSections
    
    def AsDict(self):
        return {
            'teacherId': self.GetUserID(),
            'name': self.GetUserName(),
            'sex': self.GetUserSex(),
            'phoneNumber': self.GetUserPhoneNumber(),
            'birthday': self.GetUserBirthday()
        }
        
    def GetPrimaryKey(self) -> str:
        return self.__userid
        
    def GetTeachingClassSections(self, AsDict = False):
        if not AsDict:
            return self.__teachingClassSections
        retList = []
        for classSection in self.__teachingClassSections:
            retList.append(classSection.AsDict())
        return retList
    
    def _SetTeachingClassSections(self, classes: list):
        self.__teachingClassSections = classes
    
    @staticmethod
    def FromRecord(record) -> 'Teacher':
        for i in range(len(record)):
            ele = record[i]
            if ele == None:
                raise RecordException(f"Element {i} of Student record is None or Empty")
        teacher = Teacher(record[0], record[1], record[2], record[3], record[4])
        return teacher

    @staticmethod
    def GetByID(id, AsDict = False):
        from Database.TeacherDatabase import TeacherDatabase
        
        teacher = TeacherDatabase.Get(id)
        if AsDict:
            return teacher.AsDict()
        return teacher
        
    @staticmethod
    def GetAll(AsDict = False):
        from Database.TeacherDatabase import TeacherDatabase

        teachers = TeacherDatabase.GetAll()
        if AsDict:
            return list([teacher.AsDict() for teacher in teachers])
        return teachers