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
                cls._loaded[key] = cls._FetchFromDatabase(key)
        return list(cls._loaded.values())
    
    @classmethod
    def Get(cls, pk) -> IObject:
        try:
            return cls._loaded[pk]
        except KeyError:
            cls._loaded[pk] = cls._FetchFromDatabase(pk)
            return cls._loaded[pk]
    
    @classmethod
    def Insert(cls, object : IObject):
        cls._loaded[object.GetPrimaryKey()]
    
    @classmethod
    def Delete(cls, pk):
        del cls._loaded[pk]
    
    @abstractclassmethod
    def _FetchFromDatabase(cls, pk):
        pass
    
    @abstractclassmethod
    def _FetchAllPKeys(cls) -> list:
        return []