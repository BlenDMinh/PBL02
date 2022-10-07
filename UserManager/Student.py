from dataclasses import asdict
from UserManager.User import User
from Database import StudentDatabase

class Student(User):
    def __init__(self, userid, name, sex, phone_number, birthday, classname) -> None:
        super().__init__(userid, name, sex, phone_number, birthday)
        self.__classname = classname
    
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
                studentList.append(Student(rec[0], rec[1], rec[2], rec[4], rec[5], rec[3]).AsDist())
            else:
                studentList.append(Student(rec[0], rec[1], rec[2], rec[4], rec[5], rec[3]))
        return studentList
    
    @staticmethod
    def GetStudentFromDatabase(pk, AsDict = False):
        rec = StudentDatabase.Get(pk)[0]
        student = Student(rec[0], rec[1], rec[2], rec[4], rec[5], rec[3])
        if AsDict:
            return student.AsDist()
        return student