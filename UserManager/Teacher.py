from UserManager.User import User
from IObject import IObject
from Database.TeacherDatabase import TeacherDatabase

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
