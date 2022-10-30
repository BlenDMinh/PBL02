from UserManager.User import User
from Database import StudentDatabase
from Database import ClassSectionDatabase
from Database import SubjectDatabase
from Database import Student_ClassSectionDatabase

class Student(User):
    
    __classname: str
    
    def __init__(self, userid, name, sex, phone_number, birthday, classname) -> None:
        super().__init__(userid, name, sex, phone_number, birthday)
        self.__classname = classname
    
    def __init__(self, record):
        super().__init__(record[0], record[1], record[2], record[4], record[5])
        self.__classname = record[3]
        
    
    def __str__(self):
        str = f'{self.GetUserID()} {self.GetUserName()} {self.GetUserSex()} {self.GetClassName()}'
        return str
    
    def AsDist(self):
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
    def GetAllStudentFromDatabase(AsDict = False):
        students_database = StudentDatabase.GetAll()
        studentList = []
        for rec in students_database:
            if AsDict:
                studentList.append(Student(record=rec).AsDist())
            else:
                studentList.append(Student(record=rec))
        return studentList
    
    @staticmethod
    def GetStudentFromDatabase(pk, AsDict = False):
        rec = StudentDatabase.Get(pk)
        student = Student(record=rec)
        if AsDict:
            return student.AsDist()
        return student