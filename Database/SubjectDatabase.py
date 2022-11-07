from Database import Database
from Database.IDatabase import IDatabase

class SubjectDatabase(IDatabase):
    @staticmethod
    def Get(pk):
        cur = Database.Execute(f"SELECT * FROM Subject WHERE SubjectID='{pk}'")
        return cur.fetchone()

    @staticmethod
    def GetAll():
        cur = Database.Execute(f"SELECT * FROM Subject")
        return cur.fetchall()
    
    @staticmethod
    def Insert(object):
        pass
    
    @staticmethod
    def Delete(pk):
        pass

Database.InitTable("Subject")
