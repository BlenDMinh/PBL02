from Database import Database #type: ignore
from Database.BaseDatabase import BaseDatabase
from Database.Student_ClassSectionDatabase import Student_ClassSectionDatabase
from Database.ClassSectionDatabase import ClassSectionDatabase
from UserManager.User import Student

from collections import OrderedDict

class StudentDatabase(BaseDatabase):
    
    _loaded = OrderedDict()
    __classes_loaded = []
    # _changes = []
    
    @classmethod
    def FetchFromDatabase(cls, pk, onlyObject = False):
        if pk in cls._loaded:
            student = cls._loaded[pk]
        else:
            cur = Database.Execute(f"SELECT StudentID, Name, Sex, Class, PhoneNumber, Birthday FROM Student WHERE StudentID = \'{pk}\'", Debug = False)
            rec = cur.fetchone()
            student = Student.FromRecord(rec)
        
        if not onlyObject:
            classIDs = Student_ClassSectionDatabase.GetByStudentID(pk)
            classList = []
            for classID in classIDs:
                ClassSectionDatabase.FetchFromDatabase(classID, True)
                classSection = ClassSectionDatabase.Get(classID)
                classList.append(classSection)
            student._SetAttenedClasses(classList)
            cls.__classes_loaded.append(pk)
        
        cls._loaded[pk] = student
        return student
    
    @classmethod
    def _FetchAllPKeys(cls):
        cur = Database.Execute(f"SELECT StudentID FROM Student", Debug=False)
        return list(r[0] for r in cur.fetchall())
    
    @classmethod
    def IsClassesLoaded(cls, pk):
        return pk in cls.__classes_loaded
    
    @staticmethod
    def Login(id, password):
        cur = Database.Execute(f"SELECT * FROM Student WHERE StudentID='{id}' AND Password='{password}'", Debug = False)
        return len(cur.fetchall()) > 0

Database.InitTable("Student")