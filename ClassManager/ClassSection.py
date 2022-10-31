from datetime import datetime
from ClassManager.Subject import Subject
from UserManager.Teacher import Teacher

class ClassSection:
    __sectionID: str
    __subjectID: str
    __teacherID: str
    __start_time: int
    __end_time: int
    __capacity: int

    def __init__(self, sectionID, subjectID, teacherID, start_time, end_time, capacity):
        self.__sectionID = sectionID
        self.__subjectID = subjectID
        self.__teacherID = teacherID
        self.__start_time = start_time
        self.__end_time = end_time
        self.__capacity = capacity
    
    def AsDict(self):
        return {
            "sectionID": self.GetClassSectionID(),
            "subjectName": self.GetSubjectName(),
            "teacherName": self.GetTeacherName(),
            "startTime": self.GetPeriodTime()[0],
            "endTime": self.GetPeriodTime()[1],
            "capacity": self.GetClassCapacity()
        }
    
    def GetClassSectionID(self):
        return self.__sectionID
    
    def GetSubjectID(self):
        return self.__subjectID
    
    def GetSubjectName(self):
        return Subject.GetSubjectByID(self.GetSubjectID()).GetSubjectName()
    
    def GetTeacherID(self):
        return self.__teacherID
    
    def GetTeacherName(self):
        return Teacher.GetTeacherFromDatabase(self.GetTeacherID()).GetUserName()
    
    def GetClassCapacity(self):
        return self.__capacity
    
    def GetPeriodTime(self):
        return (self.__start_time, self.__end_time)

    @staticmethod
    def FromRecord(record, AsDict=False):
        pass

    @staticmethod
    def GetClassByID(id, AsDict = False):
        if AsDict:
            return ClassSection('000000000000000000', '000000000', '000000001', 1, 3, 30).AsDict()
        return ClassSection('000000000000000000', '000000000', '000000001', 1, 3, 30)
    
    @staticmethod
    def GetAllClasses(AsDict = False):
        if AsDict:
            return [ClassSection('000000000000000000', '000000000', '000000001', 1, 3, 30).AsDict()]
        return [ClassSection('000000000000000000', '000000000', '000000001', 1, 3, 30)]