from Database import Database

def GetAll():
    cur = Database.Execute("SELECT TeacherID, Name FROM Teacher")
    return cur.fetchall()

def Get(pk):
    cur = Database.Execute(f"SELECT TeacherID, Name FROM Teacher WHERE TeacherID={pk}")
    return cur.fetchone()



Database.InitTable("Teacher")