from UserInterface import UserInterface
from BusinessLogic import BusinessLogic
from Persistency import Persistency

if __name__ == "__main__":
    persistency = Persistency.VehiclePersistency()
    businessLogic = BusinessLogic.VehicleBL(persistency)
    UserInterface.UI(businessLogic)
