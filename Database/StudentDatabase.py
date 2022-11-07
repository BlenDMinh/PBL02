from Database import Database
from Database.IDatabase import IDatabase

class StudentDatabase(IDatabase):
    
    @staticmethod
    def Insert(object):
        pass

    @staticmethod
    def Delete(pk):
        pass

    @staticmethod
    def Get(pk):
        cur = Database.Execute(f"SELECT StudentID, Name, Sex, Class, PhoneNumber, Birthday FROM Student WHERE StudentID = {pk}")
        return cur.fetchone()

    @staticmethod
    def GetAll():
        cur = Database.Execute("SELECT StudentID, Name, Sex, Class, PhoneNumber, Birthday FROM Student")
        return cur.fetchall()

    @staticmethod
    def Login(id, password):
        cur = Database.Execute(f"SELECT * FROM Student WHERE StudentID='{id}' AND Password='{password}'")
        return len(cur.fetchall()) > 0

Database.InitTable("Student")