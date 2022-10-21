from Database import Database

def AddToken(token):
    Database.Execute(f"INSERT INTO Token (token) VALUES ('{token}')")

def HasToken(token):
    cur = Database.Execute(f"SELECT * FROM Token WHERE token='{token}'")
    if len(cur.fetchall()) > 0:
        return True
    return False

def RemoveToken(token):
    Database.Execute(f"DELETE FROM Token WHERE token='{token}'")

Database.InitTable("Token")