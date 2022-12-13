from abc import ABC, abstractmethod

class Base(ABC):
    def F(self):
        print(self.DoThis())
        
    @abstractmethod
    def DoThis(self):
        pass

class Derived(Base):
    
    def DoThis(self):
        return 5

a = Derived()
a.F()