from re import sub
from Database import SubjectDatabase

class Subject:
    __subjectID: str
    __subjectName: str
    
    def __init__(self):
        pass
    def __init__(self, subjectID, subjectName):
        self.__subjectID = subjectID
        self.__subjectName = subjectName
        
    def __init__(self, record):
        
        pass
    
    def GetSubjectID(self):
        return self.__subjectID
    
    def GetSubjectName(self):
        return self.__subjectName
