from Database import Database # type: ignore
from Interface import IDatabase

class TokenDatabase(IDatabase):    
    @staticmethod
    def Insert(object):
        Database.Execute(f"INSERT INTO Token (token, UserID) VALUES ('{object['token']}', '{object['userid']}')", Debug = False)

    @staticmethod
    def Get(pk):
        cur = Database.Execute(f"SELECT UserID FROM Token WHERE token='{pk}'", Debug = False)
        data = cur.fetchone()
        if data != None:
            return data[0]
        return None

    @staticmethod
    def GetAll():
        return None

    @staticmethod
    def Delete(pk):
        Database.Execute(f"DELETE FROM Token WHERE token='{pk}'", Debug = False)

Database.InitTable("Token")