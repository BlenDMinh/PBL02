from abc import ABC, abstractstaticmethod, abstractmethod

class IObject(ABC):
    
    @abstractmethod
    def AsDict(self) -> dict:
        pass
    
    @abstractstaticmethod
    def FromRecord(record, AsDict=False):
        pass
    
    @abstractstaticmethod
    def GetAllFromDatabase(AsDict=False):
        pass
    
    @abstractstaticmethod
    def GetByIDFromDatabase(id, AsDict=False):
        pass

class IDatabase():
    @abstractstaticmethod
    def GetAll():
        pass
    
    @abstractstaticmethod
    def Get(pk):
        pass
    
    @abstractstaticmethod
    def Insert(object):
        pass
    
    @staticmethod
    def Delete(pk):
        pass
    