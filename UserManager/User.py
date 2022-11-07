from mimetypes import init
from enum import IntEnum
import hashlib
from datetime import datetime
from Database.TokenDatabase import TokenDatabase
import UserManager
from Database.StudentDatabase import StudentDatabase

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
            return UserManager.Student.Student.GetByIDFromDatabase(UserID, AsDict=True)  # type: ignore
        return ''

    @staticmethod
    def TokenLogout(token):
        TokenDatabase.Delete(token)
        