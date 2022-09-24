from StudentManager.User import User

class Student(User):
    def __init__(self, userid, name, sex, phone_number, birthday, classname) -> None:
        super().__init__(userid, name, sex, phone_number, birthday)
        self.__classname = classname
    
    def __str__(self):
        str = f'{self.GetUserID()} {self.GetUserName()} {self.GetUserSex()} {self.GetClassName()}'
        return str
    
    def GetClassName(self):
        return self.__classname