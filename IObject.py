from abc import ABC, abstractstaticmethod, abstractmethod

class IObject(ABC):
    
    @abstractmethod
    def AsDict() -> dict:
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