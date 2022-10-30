from Database import Database

def Add():
    pass

def Delete(pk):
    pass

def Get(pk):
    cur = Database.Execute(f"SELECT StudentID, Name, Sex, Class, PhoneNumber, Birthday FROM Student WHERE StudentID = {pk}")
    return cur.fetchone()

def GetAll():
    cur = Database.Execute("SELECT StudentID, Name, Sex, Class, PhoneNumber, Birthday FROM Student")
    return cur.fetchall()

def Login(id, password):
    cur = Database.Execute(f"SELECT * FROM Student WHERE StudentID='{id}' AND Password='{password}'")
    return len(cur.fetchall()) > 0

Database.InitTable("Student")