from UserInterface import VehicleUI
from BusinessLogic import VehicleBL
from Persistency import VehiclePersistency

if __name__ == "__main__":
    persistency = VehiclePersistency.VehiclePersistency()
    businessLogic = VehicleBL.VehicleBL(persistency)
    VehicleUI.VehicleUI(businessLogic)
