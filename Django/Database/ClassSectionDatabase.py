from Database import Database  # type: ignore
from Database.BaseDatabase import BaseDatabase
from Database.Student_ClassSectionDatabase import Student_ClassSectionDatabase
from ClassManager.ClassSection import ClassSection

class ClassSectionDatabase(BaseDatabase):
    
    _loaded = dict()
    _changes = []
    
    @classmethod
    def _FetchFromDatabase(cls, pk):
        cur = Database.Execute(f"SELECT * FROM ClassSection WHERE SectionID  = '{pk}'", Debug = False)
        
        rec = cur.fetchone()
        studentList = Student_ClassSectionDatabase.GetBySectionID(rec[0])
        
        classSection = ClassSection.FromRecord((*rec, studentList))
        return classSection
    
    @classmethod
    def _FetchAllPKeys(cls):
        cur = Database.Execute(f"SELECT SectionID FROM ClassSection", Debug=False)
        return list(r[0] for r in cur.fetchall())

Database.InitTable('ClassSection')