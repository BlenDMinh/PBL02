from dataclasses import asdict
from UserManager.User import User
from IObject import IObject
from Database.StudentDatabase import StudentDatabase
from Database import ClassSectionDatabase
from Database import SubjectDatabase
from Database import Student_ClassSectionDatabase

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