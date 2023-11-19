from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def Save(self, vehicleData):
        pass    

    @abstractmethod
    def Load(self, vehicleData):
        pass