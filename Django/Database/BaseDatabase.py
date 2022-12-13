from abc import ABC, abstractmethod

class BaseDatabase(ABC):
    
    __loaded = dict()
    __changes = []
    
    def GetAll(self):
        keys = self._FetchAllPKeys()
        for key in keys: 
            if key not in self.__loaded:
                self.__loaded[key] = self._FetchFromDatabase(key)
        return list(self.__loaded.values())
    
    def Get(self, pk):
        try:
            return self.__loaded[pk]
        except KeyError:
            self.__loaded[pk] = self._FetchFromDatabase(pk)
            return self.__loaded[pk]
    
    @abstractmethod
    def _FetchFromDatabase(self, pk):
        pass
    
    @abstractmethod
    def _FetchAllPKeys(self) -> list:
        pass
    
    @staticmethod
    def Insert(object):
        pass
    
    @staticmethod
    def Update(object):
        pass
    
    @staticmethod
    def Delete(pk):
        pass