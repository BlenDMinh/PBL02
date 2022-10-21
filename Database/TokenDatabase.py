from Database import Database

def AddToken(token):
    Database.Execute(f"INSERT INTO 'Token' VALUES ('{token}')").fetchone()

def HasToken(token):
    cur = Database.Execute(f"SELECT * FROM 'Token' WHERE 'Token'.tokenHash='{token}'")
    if len(cur.fetchall()) > 0:
        return True
    return False

def RemoveToken(token):
    Database.Execute(f"DELETE FROM 'Token' WHERE 'Token'.tokenHash='{token}'").fetchone()

Database.InitTable("Token")