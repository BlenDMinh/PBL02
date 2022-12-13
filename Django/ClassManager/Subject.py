from Interface import IObject
from Database.SubjectDatabase import SubjectDatabase

class Subject(IObject):
    __subjectID: str
    __subjectName: str
    
    def __init__(self, subjectID, subjectName):
        self.__subjectID = subjectID
        self.__subjectName = subjectName
    
    def AsDict(self):
        return {
            "subjectID": self.GetSubjectID(),
            "subjectName": self.GetSubjectName()
        }

    def GetSubjectID(self):
        return self.__subjectID
    
    def GetSubjectName(self):
        return self.__subjectName
    
    def SetSubjectName(self, subjectName : str):
        self.__subjectName = subjectName
    
    @staticmethod
    def FromRecord(record, AsDict=False):
        subjectID = record[0]
        subjectName = record[1]
        subject = Subject(subjectID, subjectName)
        if AsDict:
            return subject.AsDict()
        return subject

    @staticmethod
    def GetByID(id, AsDict=False):
        rec = SubjectDatabase.Get(id)
        return Subject.FromRecord(rec, AsDict=AsDict)
    
    @staticmethod
    def GetAll(AsDict=False):
        data = SubjectDatabase.GetAll()
        subjects = []
        for rec in data:
            subjects.append(Subject.FromRecord(rec, AsDict=AsDict))
        return subjects
