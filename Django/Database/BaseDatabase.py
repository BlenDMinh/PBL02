from abc import ABC, abstractmethod, abstractclassmethod
from Interface import IObject

class BaseDatabase(ABC):
    
    _loaded = dict()
    _changes = []
    
    @classmethod
    def GetAll(cls) -> list[IObject]:
        keys = cls._FetchAllPKeys()
        for key in keys: 
            if key not in cls._loaded:
                cls.FetchFromDatabase(key, True)
        return list(cls._loaded.values())
    
    @classmethod
    def Get(cls, pk) -> IObject:
        try:
            return cls._loaded[pk]
        except KeyError:
            cls.FetchFromDatabase(pk, True)
            return cls._loaded[pk]
    
    @classmethod
    def Insert(cls, object : IObject):
        cls._loaded[object.GetPrimaryKey()] = object
    
    @classmethod
    def Delete(cls, pk):
        del cls._loaded[pk]
    
    @abstractclassmethod
    def FetchFromDatabase(cls, pk, onlyObject = False):
        pass
    
    @abstractclassmethod
    def _FetchAllPKeys(cls) -> list:
        return []