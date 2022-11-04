from Database import Database

def GetByID(id):
    cur = Database.Execute(f'SELECT * FROM Subject WHERE SubjectID=\'{id}\'')
    return cur.fetchone()

Database.InitTable("Subject")