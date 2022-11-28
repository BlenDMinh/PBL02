class IObject():
    
    def AsDict(self) -> dict:
        raise NotImplementedError()
    
    @staticmethod
    def FromRecord(record, AsDict=False):
        raise NotImplementedError()
    
    @staticmethod
    def GetAllFromDatabase(AsDict=False):
        raise NotImplementedError()
    
    @staticmethod
    def GetByIDFromDatabase(id, AsDict=False):
        raise NotImplementedError()

class IDatabase():
    @staticmethod
    def GetAll():
        raise NotImplementedError()
    
    @staticmethod
    def Get(pk):
        raise NotImplementedError()
    
    @staticmethod
    def Insert(object):
        raise NotImplementedError()
    
    @staticmethod
    def Delete(pk):
        raise NotImplementedError()
    