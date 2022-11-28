from Database import Database
from Interface import IDatabase

class StudentDatabase(IDatabase):
    
    @staticmethod
    def Insert(object):
        pass

    @staticmethod
    def Delete(pk):
        pass

    @staticmethod
    def Get(pk):
        cur = Database.Execute(f"SELECT StudentID, Name, Sex, Class, PhoneNumber, Birthday FROM Student WHERE StudentID = '{pk}'", Debug = False)
        return cur.fetchone()

    @staticmethod
    def GetAll():
        cur = Database.Execute("SELECT StudentID, Name, Sex, Class, PhoneNumber, Birthday FROM Student", Debug = False)
        return cur.fetchall()

    @staticmethod
    def Login(id, password):
        cur = Database.Execute(f"SELECT * FROM Student WHERE StudentID='{id}' AND Password='{password}'", Debug = False)
        return len(cur.fetchall()) > 0

Database.InitTable("Student")