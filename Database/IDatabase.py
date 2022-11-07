from abc import ABC, abstractmethod, abstractstaticmethod

class IDatabase(ABC):
    @abstractstaticmethod
    def GetAll():
        pass
    
    @abstractstaticmethod
    def Get(pk):
        pass
    
    @abstractstaticmethod
    def Insert(object):
        pass
    
    @abstractstaticmethod
    def Delete(pk):
        pass
    