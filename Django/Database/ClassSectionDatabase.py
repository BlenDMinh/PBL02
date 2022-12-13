from Database import Database  # type: ignore
from Database.BaseDatabase import BaseDatabase

class ClassSectionDatabase(BaseDatabase):
    
    def _FetchFromDatabase(self, pk):
        cur = Database.Execute(f"SELECT * FROM ClassSection WHERE SectionID  = '{pk}'", Debug = False)
        return cur.fetchone()
    
    def _FetchAllPKeys(self):
        cur = Database.Execute(f"SELECT SectionID FROM ClassSection", Debug=False)
        return list(r[0] for r in cur.fetchall())

Database.InitTable('ClassSection')