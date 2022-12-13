from Database import Database #type: ignore
from Interface import IDatabase

class Student_ClassSectionDatabase(IDatabase):
    @staticmethod
    def GetByStudentID(studentID):
        cur = Database.Execute(f'SELECT ClassSection.SectionID FROM (SELECT * FROM Student_ClassSection WHERE StudentID = \'{studentID}\') as a INNER JOIN ClassSection ON a.SectionID = ClassSection.SectionID', Debug=False)
        return cur.fetchall()

    @staticmethod
    def GetBySectionID(sectionID):
        cur = Database.Execute(f'SELECT Student.StudentID FROM (SELECT * FROM Student_ClassSection WHERE SectionID = \'{sectionID}\') as a INNER JOIN Student ON a.StudentID = Student.StudentID', Debug = False)

    @staticmethod 
    def CountBySectionID(sectionID):
        cur = Database.Execute(f"SELECT count(*) FROM Student_ClassSection WHERE SectionID = \'{sectionID}\'", Debug = False)
        return cur.fetchone()[0]

    @staticmethod
    def CountByStudentID(studentID):
        cur = Database.Execute(f"SELECT count(*) FROM Student_ClassSection WHERE StudentID = \'{studentID}\'", Debug = False)
        return cur.fetchone()[0]
    
    @staticmethod
    def Insert(object):
        Database.Execute(f"INSERT INTO Student_ClassSection VALUES (\'{object[0]}\',\'{object[1]}\')", Debug = False)

    @staticmethod
    def Delete(pk):
        Database.Execute(f"DELETE FROM Student_ClassSection WHERE StudentID  = \'{pk[0]}\' and SectionID = \'{pk[1]}\'")

    @staticmethod
    def Get(pk):
        pass

    @staticmethod
    def GetAll():
        pass
    
Database.InitTable('Student_ClassSection')