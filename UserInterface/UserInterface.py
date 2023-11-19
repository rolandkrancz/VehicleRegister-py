from BusinessLogic import VehicleData

class UI:
    BL = 0
    def __init__(self, businessLogic):
        self.BL = businessLogic
        self.DisplayMainMenu()

    def DisplayMainMenu(self):
        while True:
            print("\n1. Add Vehicle Record")
            print("2. Get Vehicle Info")
            print("3. Exit\n")
            selection = input()

            if (selection == '1'):
                self._AddRecord()
            elif (selection == '2'):
                self._GetVehicleInfo()
            elif (selection == '3'):
                break;
    
    def _AddRecord(self):
        reg_number = input("Enter registration number: ")
        model = input("Enter model: ")
        type = input("Enter type: ")
        name = input("Enter owner's name: ")
        address = input("Enter owner's address: ")
        record = VehicleData.VehicleData(reg_number, model, type, name, address)
        self.BL.RegisterVehicle(record)

    def _GetVehicleInfo(self):
        registrationNumber = input("Enter registration number: ")

        vehicle_data = self.BL.GetVehicleInfo(registrationNumber)

        if vehicle_data:
            print("Registration Number:", vehicle_data.registration_number)
            print("Model:", vehicle_data.model)
            print("Type:", vehicle_data.type)
            print("Owner's Name:", vehicle_data.name)
            print("Owner's Address:", vehicle_data.address)
        else:
            print("Vehicle not found.")
