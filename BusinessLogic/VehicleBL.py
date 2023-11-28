class VehicleBL:
    storage = 0
    def __init__(self, storage):
        self.storage = storage
    
    def RegisterVehicle(self, vehicleData):
        self.storage.Save(vehicleData)

    def GetVehicleInfo(self, registrationNumber):
        return self.storage.Load(registrationNumber)