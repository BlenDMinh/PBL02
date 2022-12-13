from Database import Database #type: ignore
from Database.BaseDatabase import BaseDatabase

class SubjectDatabase(BaseDatabase):
    def _FetchFromDatabase(self, pk):
        cur = Database.Execute(f"SELECT * FROM Subject WHERE SubjectID = '{pk}'", Debug = False)
        return cur.fetchone()
    
    def _FetchAllPKeys(self):
        cur = Database.Execute(f"SELECT SubjectID FROM Subject", Debug=False)
        return list(r[0] for r in cur.fetchall())


Database.InitTable("Subject")
