from BusinessLogic import VehicleEntity
from BusinessLogic import StorageInterface

class VehiclePersistency(StorageInterface.IStorage):
    def Save(self, vehicleData):
        with open('database.txt', 'a') as file:
            file.write(f"{vehicleData.registration_number}, {vehicleData.model}, {vehicleData.type}, {vehicleData.name}, {vehicleData.address}\n")

    def Load(self, registrationNumber):
        with open('database.txt', 'r') as file:
            for line in file:
                data = line.strip().split(', ')
                if data[0] == registrationNumber:
                    return VehicleEntity.VehicleEntity(data[0], data[1], data[2], data[3], data[4])
        return None
