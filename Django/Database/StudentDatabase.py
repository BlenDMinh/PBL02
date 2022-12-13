from Database import Database #type: ignore
from Database.BaseDatabase import BaseDatabase
from Database.Student_ClassSectionDatabase import Student_ClassSectionDatabase
from Database.ClassSectionDatabase import ClassSectionDatabase
from UserManager.User import Student

class StudentDatabase(BaseDatabase):
    
    _loaded = dict()
    _changes = []
    
    @classmethod
    def _FetchFromDatabase(cls, pk):
        cur = Database.Execute(f"SELECT StudentID, Name, Sex, Class, PhoneNumber, Birthday FROM Student WHERE StudentID = '{pk}'", Debug = False)
        
        rec = cur.fetchone()
        classList = Student_ClassSectionDatabase.GetByStudentID(rec[0])
        
        student = Student.FromRecord((*rec, classList))
        
        
        return student
    
    @classmethod
    def _FetchAllPKeys(cls):
        cur = Database.Execute(f"SELECT StudentID FROM Student", Debug=False)
        return list(r[0] for r in cur.fetchall())
    
    @staticmethod
    def Login(id, password):
        cur = Database.Execute(f"SELECT * FROM Student WHERE StudentID='{id}' AND Password='{password}'", Debug = False)
        return len(cur.fetchall()) > 0

Database.InitTable("Student")