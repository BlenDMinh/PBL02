from UserManager.User import User

class Teacher(User):
    def AsDict(self):
        return {
            'teacherId': self.GetUserID(),
            'name': self.GetUserName(),
            'sex': self.GetUserSex(),
            'phoneNumber': self.GetUserPhoneNumber(),
            'birthday': self.GetUserBirthday()
        }
    
    @staticmethod
    def GetTeacherFromDatabase(pk, AsDict = False):
        pass

    @staticmethod
    def GetAllTeacherFromDatabase(AsDict = False):
        pass
