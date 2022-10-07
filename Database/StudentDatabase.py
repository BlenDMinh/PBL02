from Database import Database

def Add():
    pass

def Delete(pk):
    pass

def Get(pk):
    cur = Database.Execute(f"SELECT StudentID, Name, Sex, Class, PhoneNumber, Birthday FROM Student WHERE StudentID = {pk}")
    return cur.fetchall()

def GetAll():
    cur = Database.Execute("SELECT StudentID, Name, Sex, Class, PhoneNumber, Birthday FROM Student")
    return cur.fetchall()

def Login(username, password):
    pass

Database.InitTable("Student")