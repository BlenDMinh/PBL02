from Database import Database
from Database.IDatabase import IDatabase

class Student_ClassSectionDatabase(IDatabase):
    @staticmethod
    def GetByStudentID(studentID):
        cur = Database.Execute(f'SELECT ClassSection.* FROM (SELECT * FROM Student_ClassSection WHERE StudentID = \'{studentID}\') as a INNER JOIN ClassSection ON a.SectionID = ClassSection.SectionID')
        return cur.fetchall()

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
