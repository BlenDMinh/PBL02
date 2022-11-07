from Database import Database
from Database.IDatabase import IDatabase

class TeacherDatabase(IDatabase):
    @staticmethod
    def GetAll():
        cur = Database.Execute("SELECT TeacherID, Name FROM Teacher")
        return cur.fetchall()

    @staticmethod
    def Get(pk):
        cur = Database.Execute(f"SELECT TeacherID, Name FROM Teacher WHERE TeacherID={pk}")
        return cur.fetchone()
    
    @staticmethod
    def Insert(object):
        pass
    
    @staticmethod
    def Delete(pk):
        pass

Database.InitTable("Teacher")