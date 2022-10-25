from datetime import datetime

class ClassSection:
    __sectionID: str
    __subjectID: str
    __teacherID: str
    __start_time: int
    __end_time: int
    __capacity: int
    
    def __init__(self):
        pass
    
    def GetClassSectionID(self):
        return self.__sectionID
    
    def GetSubjectID(self):
        return self.__subjectID
    
    def GetTeacherID(self):
        return self.__teacherID
    
    def GetClassCapacity(self):
        return self.__capacity
    