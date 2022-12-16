from Database import Database  # type: ignore
from Database.BaseDatabase import BaseDatabase
from UserManager.User import Teacher

class TeacherDatabase(BaseDatabase):
    
    _loaded = dict()
    __classes_loaded = []
    # _changes = []
    
    @classmethod
    def FetchFromDatabase(cls, pk, onlyObject = False):
        if pk in cls._loaded:
            teacher = cls._loaded[pk]
        else:
            cur = Database.Execute(f"SELECT * FROM Teacher WHERE TeacherID='{pk}'", Debug = False)
            teacher = Teacher.FromRecord(cur.fetchone())
        
        if not onlyObject:
            cur = Database.Execute(f"SELECT SectionID FROM ClassSection WHERE TeacherID='{pk}'", Debug = False)
            classIDs = [k[0] for k in cur.fetchall()]
            classList = []
            
            from Database.ClassSectionDatabase import ClassSectionDatabase
            
            for classID in classIDs:
                ClassSectionDatabase.FetchFromDatabase(classID, True)
                classList.append(ClassSectionDatabase.Get(classID))
            teacher._SetTeachingClassSections(classList)
            cls.__classes_loaded.append(pk)
        cls._loaded[pk] = teacher
        return teacher
    
    @classmethod
    def _FetchAllPKeys(cls):
        cur = Database.Execute(f"SELECT TeacherID FROM Teacher", Debug=False)
        return list(r[0] for r in cur.fetchall())


Database.InitTable("Teacher")
