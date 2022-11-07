from Database.SubjectDatabase import SubjectDatabase

class Subject:
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
    
    @staticmethod
    def FromRecord(record, AsDict=False):
        subjectID = record[0]
        subjectName = record[1]
        subject = Subject(subjectID, subjectName)
        if AsDict:
            return subject.AsDict()
        return subject

    @staticmethod
    def GetSubjectByID(id, AsDict=False):
        rec = SubjectDatabase.Get(id)
        return Subject.FromRecord(rec, AsDict=AsDict)
