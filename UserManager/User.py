from mimetypes import init
from enum import IntEnum

class Sex(IntEnum):
    MALE = 0
    FEMALE = 1
    OTHER = 2

class User:
    
    def __init__(self):
        pass
    def __init__(self, userid, name, sex, phone_number, birthday):
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
    