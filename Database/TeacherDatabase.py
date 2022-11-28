from Database import Database
from Interface import IDatabase

class TeacherDatabase(IDatabase):
    @staticmethod
    def GetAll():
        cur = Database.Execute("SELECT * FROM Teacher", Debug=False)
        return cur.fetchall()

    @staticmethod
    def Get(pk):
        cur = Database.Execute(f"SELECT * FROM Teacher WHERE TeacherID='{pk}'", Debug=False)
        return cur.fetchone()
    
    @staticmethod
    def Insert(object):
        pass
    
    @staticmethod
    def Delete(pk):
        pass

Database.InitTable("Teacher")
