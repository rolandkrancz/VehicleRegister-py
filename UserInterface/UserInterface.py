from BusinessLogic import BusinessLogic
from BusinessLogic import VehicleData
from Persistency import Persistency

def DisplayMainMenu():
    while True:
        print("\n1. Add Vehicle Record")
        print("2. Get Vehicle Info")
        print("3. Exit\n")
        selection = input()
        
        if (selection == '1'):
            AddRecord()
        elif (selection == '2'):
            GetVehicleInfo()
        elif (selection == '3'):
            break;
    
def AddRecord():
    reg_number = input("Enter registration number: ")
    model = input("Enter model: ")
    type = input("Enter type: ")
    name = input("Enter owner's name: ")
    address = input("Enter owner's address: ")
    record = VehicleData.VehicleData(reg_number, model, type, name, address)
    businessLogic = BusinessLogic.VehicleBL(Persistency.VehiclePersistency())
    businessLogic.RegisterVehicle(record)

def GetVehicleInfo():
    registrationNumber = input("Enter registration number: ")
    
    businessLogic = BusinessLogic.VehicleBL(Persistency.VehiclePersistency())
    vehicle_data = businessLogic.GetVehicleInfo(registrationNumber)
    
    if vehicle_data:
        print("Registration Number:", vehicle_data.registration_number)
        print("Model:", vehicle_data.model)
        print("Type:", vehicle_data.type)
        print("Owner's Name:", vehicle_data.name)
        print("Owner's Address:", vehicle_data.address)
    else:
        print("Vehicle not found.")
