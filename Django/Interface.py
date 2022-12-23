from abc import ABC, abstractstaticmethod, abstractmethod


class IObject(ABC):

    @abstractmethod
    def AsDict(self) -> dict:
        pass

    @abstractmethod
    def GetPrimaryKey(self) -> str:
        pass

    @abstractstaticmethod
    def FromRecord(record):
        pass

    @abstractstaticmethod
    def GetAll(AsDict=False):
        pass

    @abstractstaticmethod
    def GetByID(id, AsDict=False):
        pass


class IDatabase():

    __loaded = dict()
    __changes = []

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
    def Update(object):
        pass

    @abstractstaticmethod
    def Delete(pk):
        pass

    @abstractstaticmethod
    def CommitChanges():
        pass
