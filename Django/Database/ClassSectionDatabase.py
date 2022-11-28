from Database import Database  # type: ignore
from Interface import IDatabase

class ClassSectionDatabase(IDatabase):

    @staticmethod
    def Get(pk):
        cur = Database.Execute(f"SELECT * FROM ClassSection WHERE SectionID  = '{pk}'")
        return cur.fetchone()

    @staticmethod
    def GetAll():
        cur = Database.Execute(f"SELECT * FROM ClassSection")
        return cur.fetchall()

    @staticmethod 
    def Insert(object):
        pass

    @staticmethod
    def Delete(pk):
        pass

Database.InitTable('ClassSection')