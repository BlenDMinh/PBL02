from Database import Database  # type: ignore
from Database.BaseDatabase import BaseDatabase
from Database.Student_ClassSectionDatabase import Student_ClassSectionDatabase
from ClassManager.ClassSection import ClassSection

from collections import OrderedDict

class ClassSectionDatabase(BaseDatabase):
    
    _loaded = OrderedDict()
    __students_loaded = []
    # _changes = []
    
    @classmethod
    def FetchFromDatabase(cls, pk, onlyObject = False):
        if pk in cls._loaded:
            classSection = cls._loaded[pk]
        else:
            cur = Database.Execute(f"SELECT * FROM ClassSection WHERE SectionID  = '{pk}'", Debug = False)
            rec = cur.fetchone()
            classSection = ClassSection.FromRecord(rec)
        
        if not onlyObject:
            studentIDs = Student_ClassSectionDatabase.GetBySectionID(pk)
            
            studentList = []
            for studentID in studentIDs:
                from Database.StudentDatabase import StudentDatabase
                StudentDatabase.FetchFromDatabase(studentID, True)
                studentList.append(StudentDatabase.Get(studentID))
            classSection._SetAttendingStudents(studentList)
            cls.__students_loaded.append(pk)
            
        cls._loaded[pk] = classSection
        
        return classSection
    
    @classmethod
    def _FetchAllPKeys(cls):
        cur = Database.Execute(f"SELECT SectionID FROM ClassSection", Debug=False)
        return list(r[0] for r in cur.fetchall())
    
    @classmethod
    def IsStudentsLoaded(cls, pk):
        return pk in cls.__students_loaded

Database.InitTable('ClassSection')