DEFAULT_DATABASE_PATH = './Database/data.sqlite3'

config = {
    "Student": {
        "properties": {
            "StudentID": "CHAR(9)",
            "Name": "NVARCHAR",
            "Sex": "BIT",
            "Class": "CHAR",
            "PhoneNumber": "CHAR(15)",
            "Birthday": "DATE",
            "Password": "CHAR",
        },
        "PRIMARY KEY": ["StudentID"]
    },
    "Teacher": {
        
    }
}