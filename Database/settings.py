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
        "properties": {
            "SubjectID": "CHAR(9)",
            "SubjectName": "NVARCHAR(255)"
        },
        "PRIMARY KEY": ["SubjectID"]
    },
    "ClassSection": {
        "properties": {
            "SectionID": "CHAR(18)",
            "SubjectID": "CHAR(9)",
            "TeacherID": "CHAR(9)",
            "Time": "VARCHAR",
            "Capacity": "INT"
        }
    },
    "Student_ClassSection": {
        "properties": {
            "StudentID": "CHAR(9)",
            "SectionID": "CHAR(9)"
        }
    },
    "Token": {
        "properties": {
            "token": "VARCHAR(128)",
            "UserID": "CHAR(9)"
        },
        "PRIMARY KEY": ["token"]
    }
}