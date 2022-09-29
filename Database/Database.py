import sqlite3
from sqlite3 import Error
from Database import settings
import traceback

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to Database")
    except Error as e:
        print(e)
    return conn

def Execute(SQLQuery):
    print(f"SQL Executing:\n{SQLQuery}")
    cur = create_connection(settings.DEFAULT_DATABASE_PATH).cursor()
    try:
        cur.execute(SQLQuery)
        return cur
    except sqlite3.IntegrityError as er:
        print('INTEGRITY ERROR\n')
        print(traceback.print_exc())

def GetAllProperties(TableName):
    data = Execute(f"SELECT * FROM {TableName}")
    return (c for c in data.description)

def InitTable(TableName):
    properties = settings.config[TableName]
    print(properties)
    # CREATE TABLE IF NOT EXIST
    if(len(properties) == 0):
        Execute(f"CREATE TABLE IF NOT EXISTS {TableName} (Empty CHAR);")
    else:
        Execute(f"CREATE TABLE IF NOT EXISTS {TableName} ({', '.join(map(lambda k: k + ' ' + properties[k], properties))});")
    
    # MODIFY TABLE
    table_properties = GetAllProperties(TableName)
    print(table_properties)
    # if(len(properties) == 0):
    #     if 'Empty' not in table_properties:
    #         Execute(f"ALTER TABLE {TableName} ADD COLUMN Empty CHAR")
    #     for property in table_properties:
    #         Execute(f"ALTER TABLE {TableName} DROP COLUMN {property}")
    # else:
        
    #     if 'Empty' in table_properties:
    #         Execute(f"ALTER TABLE {TableName} DROP IF EXISTS Empty")
        
    pass

