from Database import Database #type: ignore
from Database.BaseDatabase import BaseDatabase
from ClassManager.Subject import Subject

class SubjectDatabase(BaseDatabase):
    
    _loaded = dict()
    _changes = []
    
    @classmethod
    def FetchFromDatabase(cls, pk, onlyObject = False):
        if pk in cls._loaded:
            subject = cls._loaded[pk]
        else:
            cur = Database.Execute(f"SELECT * FROM Subject WHERE SubjectID = '{pk}'", Debug = False)
            subject = Subject.FromRecord(cur.fetchone())
            
        cls._loaded[pk] = subject
        return cls._loaded[pk]
    
    @classmethod
    def _FetchAllPKeys(cls):
        cur = Database.Execute(f"SELECT SubjectID FROM Subject", Debug=False)
        return list(r[0] for r in cur.fetchall())


Database.InitTable("Subject")
