from Database import Database #type: ignore
from Database.BaseDatabase import BaseDatabase

class StudentDatabase(BaseDatabase):
    
    def _FetchFromDatabase(self, pk):
        cur = Database.Execute(f"SELECT StudentID, Name, Sex, Class, PhoneNumber, Birthday FROM Student WHERE StudentID = '{pk}'", Debug = False)
        return cur.fetchone()
    
    def _FetchAllPKeys(self):
        cur = Database.Execute(f"SELECT StudentID FROM Student", Debug=False)
        return list(r[0] for r in cur.fetchall())
    
    @staticmethod
    def Login(id, password):
        cur = Database.Execute(f"SELECT * FROM Student WHERE StudentID='{id}' AND Password='{password}'", Debug = False)
        return len(cur.fetchall()) > 0

Database.InitTable("Student")