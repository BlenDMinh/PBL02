from UserManager.User import User
from Database import TeacherDatabase

class Teacher(User):
    
    def __init__(self, userid, name, sex, phone_number, birthday):
        super().__init__(userid, name, sex, phone_number, birthday)
    
    def __init__(self, record):
        super().__init__(record[0], record[1], record[2], record[3], record[4])
    
    def AsDict(self):
        return {
            'teacherId': self.GetUserID(),
            'name': self.GetUserName(),
            'sex': self.GetUserSex(),
            'phoneNumber': self.GetUserPhoneNumber(),
            'birthday': self.GetUserBirthday()
        }
    
    @staticmethod
    def GetTeacherFromDatabase(pk, AsDict = False):
        rec = ["000000000","Nguyễn Trương Anh Minh",0,"000000000000","01/12/2003","000000000"]
        teacher = Teacher(rec)
        if AsDict:
            return teacher.AsDict()
        return teacher
        
    @staticmethod
    def GetAllTeacherFromDatabase(AsDict = False):
        teachers_database = [["000000000","Nguyễn Trương Anh Minh",0,"000000000000","01/12/2003","000000000"],
                            ["000000001","Phạm Trung Hiếu",0,"000000000001","08/10/2003","000000001"],
                            ["000000002","Châu Diễm Hoàng",1,"000000000002","28/10/2003","000000002"],
                            ["000000003","Nguyễn Ngọc Bảo Nhân",0,"000000000003","24/07/2003","000000003"],
                            ["000000004","Đặng Ngọc Nam",0,"000000000004","25/07/2003","000000004"],
                            ["000000005","Huỳnh Hải Đăng",0,"000000000005","26/07/2003","000000005"],
                            ["000000006","Nguyễn Văn Bách",0,"000000000006","08/10/2003","000000006"]]
        teacherList = []
        for rec in teachers_database:
            if AsDict:
                teacherList.append(Teacher(rec).AsDict())
            else:
                teacherList.append(Teacher(rec))
        return teacherList
