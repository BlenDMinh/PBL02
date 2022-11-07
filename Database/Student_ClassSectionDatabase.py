from Database import Database
from Database.IDatabase import IDatabase

class Student_ClassSectionDatabase(IDatabase):
    @staticmethod
    def GetByStudentID(studentID):
        cur = Database.Execute(f'SELECT ClassSection.* FROM (SELECT * FROM Student_ClassSection WHERE StudentID = \'{studentID}\') as a INNER JOIN ClassSection ON a.SectionID = ClassSection.SectionID', Debug=False)
        return cur.fetchall()

    @staticmethod
    def GetBySectionID(sectionID):
        cur = Database.Execute(f'SELECT Student.* FROM (SELECT * FROM Student_ClassSection WHERE SectionID = \'{sectionID}\') as a INNER JOIN Student ON a.StudentID = Student.StudentID', Debug = False)

    @staticmethod 
    def CountBySectionID(sectionID):
        cur = Database.Execute(f"SELECT count(*) FROM Student_ClassSection WHERE SectionID = \'{sectionID}\'", Debug = False)
        return cur.fetchone()[0]

    @staticmethod
    def CountByStudentID(studentID):
        cur = Database.Execute(f"SELECT count(*) FROM Student_ClassSection WHERE StudentID = \'{studentID}\'", Debug = False)
        return cur.fetchone()[0]
    
    @staticmethod
    def Get(pk):
        pass

    @staticmethod
    def GetAll():
        pass

    @staticmethod
    def Insert(object):
        pass

    @staticmethod
    def Delete(pk):
        pass

Database.InitTable('Student_ClassSection')