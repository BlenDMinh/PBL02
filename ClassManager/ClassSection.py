from datetime import datetime
from msilib.schema import Class
from tracemalloc import start
import ClassManager
import UserManager

class ClassSection:
    __sectionID: str
    __subjectID: str
    __teacherID: str
    __start_time: int
    __end_time: int
    __capacity: int
    
    def __init__(self):
        pass
    
    def __init__(self, sectionID, subjectID, teacherID, start_time, end_time, capacity):
        self.__sectionID = sectionID
        self.__subjectID = subjectID
        self.__teacherID = teacherID
        self.__start_time = start_time
        self.__end_time = end_time
        self.__capacity = capacity
    
    def __init__(self, record):
         
        pass
    
    def GetClassSectionID(self):
        return self.__sectionID
    
    def GetSubjectID(self):
        return self.__subjectID
    
    def GetSubjectName(self):
        return ClassManager.Subject.GetSubjectByID(self.GetSubjectID()).GetSubjectName()
    
    def GetTeacherID(self):
        return self.__teacherID
    
    def GetTeacherName(self):
        return UserManager.Teacher.GetTeacherFromDatabase(self.GetTeacherID()).GetUserName()
    
    def GetClassCapacity(self):
        return self.__capacity
    