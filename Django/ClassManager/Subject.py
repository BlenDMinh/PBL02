from Interface import IObject
from Exception import RecordException

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
    
    def GetPrimaryKey(self) -> str:
        return self.__subjectID

    def GetSubjectID(self):
        return self.__subjectID
    
    def GetSubjectName(self):
        return self.__subjectName
    
    def SetSubjectName(self, subjectName : str):
        self.__subjectName = subjectName
    
    @staticmethod
    def FromRecord(record):
        if record == None:
            raise RecordException(f"Record for Subject is empty")
        for i in range(len(record)):
            ele = record[i]
            if ele == None:
                raise RecordException(f"Element {i} of Subject record is None or Empty")
        subjectID = record[0]
        subjectName = record[1]
        subject = Subject(subjectID, subjectName)
        return subject

    @staticmethod
    def GetByID(id, AsDict=False):
        from Database.SubjectDatabase import SubjectDatabase
        
        subject = SubjectDatabase.Get(id)
        if AsDict:
            return subject.AsDict()
        return subject
    
    @staticmethod
    def GetAll(AsDict=False):
        from Database.SubjectDatabase import SubjectDatabase
        
        subjects = SubjectDatabase.GetAll()
        if AsDict:
            return list([subject.AsDict() for subject in subjects])
        return subjects
