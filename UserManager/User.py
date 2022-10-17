from enum import IntEnum

class Sex(IntEnum):
    MALE = 0
    FEMALE = 1
    OTHER = 2

class User:
    
    __userid: str
    __name: str
    __sex: Sex
    __phone_number: str
    __birthday: str
    
    def __init__(self):
        pass
    def __init__(self, userid, name, sex, phone_number, birthday):
        self.__userid = userid
        self.__name = name
        self.__sex = sex
        self.__phone_number = phone_number
        self.__birthday = birthday
    
    def AsDict(self):
        return {
            'userId': self.GetUserID(),
            'name': self.GetUserName(),
            'sex': self.GetUserSex(),
            'phoneNumber': self.GetUserPhoneNumber(),
            'birthday': self.GetUserBirthday()
        }
    
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
    
    
    