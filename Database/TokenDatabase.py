from xml.sax.handler import DTDHandler
from Database import Database

def AddToken(token, userid):
    Database.Execute(f"INSERT INTO Token (token, UserID) VALUES ('{token}', '{userid}')")

def HasToken(token):
    cur = Database.Execute(f"SELECT * FROM Token WHERE token='{token}'")
    data = cur.fetchone()
    if data != None:
        print(data)
        return data[1]
    return None

def RemoveToken(token):
    Database.Execute(f"DELETE FROM Token WHERE token='{token}'")

Database.InitTable("Token")