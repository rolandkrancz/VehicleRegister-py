from abc import ABC, abstractmethod

class IStorage(ABC):
    @abstractmethod
    def Save(self, vehicleData):
        pass    

    @abstractmethod
    def Load(self, vehicleData):
        pass