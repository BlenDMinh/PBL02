from Database import SubjectDatabase

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
        pass

    @staticmethod
    def GetSubjectByID(id, AsDict=False):
        if AsDict:
            return Subject("00", "OOP").AsDict()
        return Subject("00", "OOP")
