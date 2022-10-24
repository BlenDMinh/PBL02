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
        "properties": {
            "TeacherID": "CHAR(9)",
            "Name": "NVARCHAR",
            "Sex": "BIT",
            "PhoneNumber": "CHAR(15)",
            "Birthday": "DATE",
            "Password": "CHAR",
        },
        "PRIMARY KEY": ["TeacherID"]
    },
    "Subject": {
        
    },
    "ClassSection": {
        
    },
    "Student_ClassSection": {
        
    },
    "Token": {
        "properties": {
            "token": "CHAR",
            "UserID": "CHAR(9)"
        },
        "PRIMARY KEY": ["token"]
    }
}