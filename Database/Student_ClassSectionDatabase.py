from Database import Database

def GetByStudentID(studentID):
    cur = Database.Execute(f'SELECT ClassSection.* FROM (SELECT * FROM Student_ClassSection WHERE StudentID = \'{studentID}\') as a INNER JOIN ClassSection ON a.SectionID = ClassSection.SectionID')
    return cur.fetchall()

def GetAll():
    pass

Database.InitTable('Student_ClassSection')