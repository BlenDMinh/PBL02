from Database import Database  # type: ignore
from Database.BaseDatabase import BaseDatabase

class TeacherDatabase(BaseDatabase):
    
    def _FetchFromDatabase(self, pk):
        cur = Database.Execute(f"SELECT * FROM Teacher WHERE TeacherID='{pk}'", Debug = False)
        return cur.fetchone()
    
    def _FetchAllPKeys(self):
        cur = Database.Execute(f"SELECT TeacherID FROM Teacher", Debug=False)
        return list(r[0] for r in cur.fetchall())


Database.InitTable("Teacher")
