from Database import Database  # type: ignore
from Database.BaseDatabase import BaseDatabase
from UserManager.User import Teacher

class TeacherDatabase(BaseDatabase):
    
    _loaded = dict()
    _changes = []
    
    @classmethod
    def _FetchFromDatabase(cls, pk):
        cur = Database.Execute(f"SELECT * FROM Teacher WHERE TeacherID='{pk}'", Debug = False)
        
        teacher = Teacher.FromRecord(cur.fetchone())
        return teacher
    
    @classmethod
    def _FetchAllPKeys(cls):
        cur = Database.Execute(f"SELECT TeacherID FROM Teacher", Debug=False)
        return list(r[0] for r in cur.fetchall())


Database.InitTable("Teacher")
