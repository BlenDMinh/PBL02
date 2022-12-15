from Interface import IObject


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
    def FromRecord(record, AsDict=False):
        subjectID = record[0]
        subjectName = record[1]
        subject = Subject(subjectID, subjectName)
        if AsDict:
            return subject.AsDict()
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
