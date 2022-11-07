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
    def InsertStudent_Section(studentID, sectionID):
        Database.Execute(f"INSERT INTO Student_ClassSection VALUES (\'{studentID}\',\'{sectionID}\')", Debug = False)

    @staticmethod
    def DeleteStudent_Section(studentID, sectionID):
        Database.Execute(f"DELETE FROM Student_ClassSection WHERE StudentID  = \'{studentID}\' and SectionID = \'{sectionID}\'")

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

<<<<<<< HEAD
Database.InitTable('Student_ClassSection')
=======
Database.InitTable('Student_ClassSection')
>>>>>>> 5e4298e73768cfad5076f5958401043450bb49ac
