from Database import Database #type: ignore
from Database.BaseDatabase import BaseDatabase
from ClassManager.Subject import Subject

class SubjectDatabase(BaseDatabase):
    
    _loaded = dict()
    _changes = []
    
    @classmethod
    def _FetchFromDatabase(cls, pk):
        cur = Database.Execute(f"SELECT * FROM Subject WHERE SubjectID = '{pk}'", Debug = False)
        return Subject.FromRecord(cur.fetchone())
    
    @classmethod
    def _FetchAllPKeys(cls):
        cur = Database.Execute(f"SELECT SubjectID FROM Subject", Debug=False)
        return list(r[0] for r in cur.fetchall())


Database.InitTable("Subject")
