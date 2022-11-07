from IObject import IObject
from ClassManager.Subject import Subject
from UserManager.Teacher import Teacher
from Database.ClassSectionDatabase import ClassSectionDatabase
from Database.Student_ClassSectionDatabase import Student_ClassSectionDatabase

class ClassSection(IObject):
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
            "current": self.GetCurrentNumberOfStudents(),
            "capacity": self.GetClassCapacity()
        }
    
    def GetClassSectionID(self):
        return self.__sectionID
    
    def GetSubjectID(self):
        return self.__subjectID
    
    def GetSubjectName(self):
        return Subject.GetSubjectByID(self.GetSubjectID()).GetSubjectName()  # type: ignore
    
    def GetTeacherID(self):
        return self.__teacherID
    
    def GetTeacherName(self):
        return Teacher.GetByIDFromDatabase(self.GetTeacherID()).GetUserName()  # type: ignore
    
    def GetCurrentNumberOfStudents(self):
        return 0
    
    def GetClassCapacity(self):
        return self.__capacity
    
    def GetPeriodTime(self):
        return (self.__start_time, self.__end_time)

    @staticmethod
    def FromRecord(record, AsDict=False):
        sectionID = record[0]
        subjectID = record[1]
        teacherID = record[2]
        if record[3] == None:
            startTime = 0
            endTime = 0
        else:
            timeData = record[3].split('-')
            startTime = int(timeData[0])
            endTime = int(timeData[1])
        capacity = record[4]
        
        classSection = ClassSection(sectionID, subjectID, teacherID, startTime, endTime, capacity)
        if AsDict:
            return classSection.AsDict()
        return classSection

    @staticmethod
    def GetByIDFromDatabase(id, AsDict = False):
        rec = ClassSectionDatabase.Get(id)
        classSection = ClassSection.FromRecord(rec, AsDict=AsDict)
        return classSection
    
    @staticmethod
    def GetAllFromDatabase(AsDict = False):
        data = ClassSectionDatabase.GetAll()
        classSections = []

        for rec in data:
            classSections.append(ClassSection.FromRecord(rec, AsDict=AsDict))
        
        return classSections
    
    @staticmethod
    def GetClassesAttendedByID(studentID, AsDict = False):
        classes = []
        data = Student_ClassSectionDatabase.GetByStudentID(studentID=studentID)
        for rec in data:
            classSection = ClassSection.FromRecord(record=rec, AsDict=AsDict)
            classes.append(classSection)
        return classes