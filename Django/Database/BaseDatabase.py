from abc import ABC, abstractmethod, abstractclassmethod
from Interface import IObject
from Exception import RecordException
from collections import OrderedDict

class BaseDatabase(ABC):
    
    _loaded = OrderedDict()
    # _changes = []
    
    @classmethod
    def GetAll(cls) -> list[IObject]:
        keys = cls._FetchAllPKeys()
        for key in keys: 
            if key not in cls._loaded:
                try:
                    cls.FetchFromDatabase(key, True)
                except RecordException as e:
                    print(e.message)
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