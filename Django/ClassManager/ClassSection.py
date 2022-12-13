from Interface import IObject
from ClassManager.Subject import Subject
from UserManager.User import Teacher

class ClassSection(IObject):
    __sectionID: str
    __subject: Subject
    __teacher: Teacher
    __start_time: int
    __end_time: int
    __capacity: int
    __attendingStudents = []

    def __init__(self, sectionID, subject, teacher, start_time, end_time, capacity, attendingStudents = []):
        self.__sectionID = sectionID
        self.__subject = subject
        self.__teacher = teacher
        self.__start_time = start_time
        self.__end_time = end_time
        self.__capacity = capacity
        self.__attendingStudents = attendingStudents
    
    def AsDict(self):
        return {
            "sectionID": self.GetClassSectionID(),
            "subjectName": self.GetSubject().GetSubjectName(),
            "teacherName": self.GetTeacher().GetUserName(),
            "startTime": self.GetPeriodTime()[0],
            "endTime": self.GetPeriodTime()[1],
            "current": self.GetCurrentNumberOfStudents(),
            "capacity": self.GetClassCapacity()
        }
    
    def GetPrimaryKey(self) -> str:
        return self.__sectionID
    
    def GetClassSectionID(self):
        return self.__sectionID
    
    def GetSubject(self) -> Subject:
        return self.__subject
    
    def GetTeacher(self) -> Teacher:
        return self.__teacher
    
    def GetCurrentNumberOfStudents(self):
        from Database.Student_ClassSectionDatabase import Student_ClassSectionDatabase
        
        return Student_ClassSectionDatabase.CountBySectionID(self.GetClassSectionID())
    
    def GetClassCapacity(self):
        return self.__capacity
    
    def GetPeriodTime(self):
        return (self.__start_time, self.__end_time)
    
    def GetAttendingStudents(self, AsDict = False):
        if not AsDict:
            return self.__attendingStudents
        
        retList = []
        for student in self.__attendingStudents:
            retList.append(student.AsDict())
        return retList

    @staticmethod
    def FromRecord(record, AsDict=False):
        sectionID = record[0]
        subject = Subject.GetByID(record[1])
        teacher = Teacher.GetByID(record[2])
        if record[3] == None:
            startTime = 0
            endTime = 0
        else:
            timeData = record[3].split('-')
            startTime = int(timeData[0])
            endTime = int(timeData[1])
        capacity = record[4]
        
        from Database.StudentDatabase import StudentDatabase
        
        studentList = []
        for pk in record[5]:
            studentList.append(StudentDatabase.Get(pk[0]))
        
        classSection = ClassSection(sectionID, subject, teacher, startTime, endTime, capacity, studentList)
        if AsDict:
            return classSection.AsDict()
        return classSection

    def AddStudent(self, studentID):
        from Database.Student_ClassSectionDatabase import Student_ClassSectionDatabase
        
        Student_ClassSectionDatabase.Insert((studentID, self.GetClassSectionID()))
        
    def RemoveStudent(self, studentID):
        from Database.Student_ClassSectionDatabase import Student_ClassSectionDatabase
        
        Student_ClassSectionDatabase.Delete((studentID, self.GetClassSectionID()))
    
    @staticmethod
    def GetByID(id, AsDict = False):
        from Database.ClassSectionDatabase import ClassSectionDatabase
        
        classSection = ClassSectionDatabase.Get(id)
        if AsDict:
            return classSection.AsDict()
        return classSection
    
    @staticmethod
    def GetAll(AsDict = False):
        from Database.ClassSectionDatabase import ClassSectionDatabase
    
        classSections = ClassSectionDatabase.GetAll()
        if AsDict:
            return list([classSection.AsDict() for classSection in classSections])
        return classSections
    
    @staticmethod
    def GetClassesAttendedByID(studentID, AsDict = False):
        from Database.Student_ClassSectionDatabase import Student_ClassSectionDatabase
        
        classes = []
        data = Student_ClassSectionDatabase.GetByStudentID(studentID=studentID)
        for rec in data:
            classSection = ClassSection.FromRecord(record=rec, AsDict=AsDict)
            classes.append(classSection)
        return classes
    
    # @staticmethod
    # def AddStudentIntoClass(sectionID, studentID):
    #     Student_ClassSectionDatabase.InsertStudent_Section(studentID, sectionID)
        
    # @staticmethod
    # def RemoveStudentFromClass(sectionID, studentID):
    #     Student_ClassSectionDatabase.DeleteStudent_Section(studentID, sectionID)