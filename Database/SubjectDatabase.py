from Database import Database
from Interface import IDatabase

class SubjectDatabase(IDatabase):
    @staticmethod
    def Get(pk):
        cur = Database.Execute(f"SELECT * FROM Subject WHERE SubjectID='{pk}'", Debug = False)
        return cur.fetchone()

    @staticmethod
    def GetAll():
        cur = Database.Execute(f"SELECT * FROM Subject", Debug = False)
        return cur.fetchall()
    
    @staticmethod
    def Insert(object):
        pass
    
    @staticmethod
    def Delete(pk):
        pass

Database.InitTable("Subject")
