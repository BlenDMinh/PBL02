import sqlite3
from sqlite3 import Error
from Database import settings  # type: ignore
import traceback

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def Execute(SQLQuery, Debug=True) -> sqlite3.Cursor:  # type: ignore
    if Debug:
        print(f"SQL Executing:\n{SQLQuery}")
    con = create_connection(settings.DEFAULT_DATABASE_PATH)  # type: ignore
    cur = con.cursor() # type: ignore
    try:
        cur.execute(SQLQuery)
        con.commit() # type: ignore
        return cur
    except sqlite3.IntegrityError as er:
        print('INTEGRITY ERROR\n')
        print(traceback.print_exc())

def GetAllProperties(TableName):
    data = Execute(f"SELECT * FROM {TableName}", Debug=False)
    return list([c[0] for c in data.description])

def GetAllTables():
    cur = Execute("SELECT name FROM sqlite_master WHERE type='table';", Debug=False)
    return list(map(lambda k: k[0], cur.fetchall()))

def InitTable(TableName):
    # print(f"Init table {TableName}")
    properties = settings.config[TableName]  # type: ignore
    # print(properties)
    # CREATE TABLE IF NOT EXIST
    tables = list(GetAllTables())
    # print(tables)
    if TableName not in tables:
        if(len(properties['properties']) == 0):
            Execute(f"CREATE TABLE IF NOT EXISTS {TableName} (Empty CHAR);", Debug=False)
        else:
            Execute(f"CREATE TABLE IF NOT EXISTS {TableName} ({', '.join(map(lambda k: k + ' ' + properties['properties'][k], properties['properties']))});", Debug=False)
            if 'PRIMARY KEY' in properties:
                Execute(f"ALTER TABLE {TableName} ADD CONSTRAINT PK_{TableName} PRIMARY KEY ({', '.join(properties['PRIMARY KEY'])})", Debug=False)
            else:
                pass
    else:
        # print('=' * 20 + f"MODIFY TABLE {TableName}" + "=" * 20)
        # MODIFY TABLE
        table_properties = GetAllProperties(TableName)
        # print(table_properties)
        if(len(properties['properties']) == 0):
            if 'Empty' not in table_properties:
                Execute(f"ALTER TABLE {TableName} ADD COLUMN Empty CHAR", Debug=False)
            for property in table_properties:
                if property != 'Empty':
                    Execute(f"ALTER TABLE {TableName} DROP COLUMN {property}", Debug=False)
        else:
            for property in properties['properties']:
                if property not in table_properties:
                    Execute(f"ALTER TABLE {TableName} ADD {property} {properties['properties'][property]}", Debug=False)
            for property in table_properties:
                if property not in properties['properties']:
                    Execute(f"ALTER TABLE {TableName} DROP COLUMN {property}", Debug=False)