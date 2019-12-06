from IO.destinationIO import DestinationIO
from IO.voyageIO import VoyageIO
from IO.planeIO import PlaneIO
from IO.employeeIO import EmployeeIO
from IO.routeIO import RouteIO
from IO.permitIO import PermitIO

class IOAPI ():

    def __init__(self):
        self.desIO = DestinationIO('IO/Data/destinations.csv') # Hardcoded filenames - Only place to change the path is here
        self.voyIO = VoyageIO('IO/Data/voyages.csv')
        self.plaIO = PlaneIO('IO/Data/planes.csv')
        self.empIO = EmployeeIO('IO/Data/Crew.csv')
        self.rouIO = RouteIO('IO/Data/routes.csv')
        self.perIO = PermitIO('IO/Data/permits.csv')
        

    def loadDestinationFromFile (self):
        return self.desIO.loadDestinationFromFile()
    
    def storeDestinationToFile(self):
        return self.desIO.storeDestinationToFile()

    def updateContactInfoInFile(self):
        return self.desIO.updateContactInfoInFile()

    def loadVoyagesFromFile (self):
        return self.voyIO.loadVoyagesFromFile()
    
    def storeVoyageToFile(self):
        return self.voyIO.storeVoyageToFile()

    def updateVoyageInFile(self):
        return self.voyIO.updateVoyageInFile()

    def loadPlanesFromFile(self):
        return self.plaIO.loadPlanesFromFiles()

    def storePlaneToFile(self):
        return self.plaIO.storePlaneToFile()

    def loadEmployeesFromFile(self):
        return self.empIO.loadFile()

    def storeEmployeeToFile(self):
        return self.empIO.storeEmployeeToFile()

    def updateEmployeeInFile(self):
        return self.empIO.updateEmployeeInFile()

    def loadRoutesFromFile(self):
        return self.rouIO.loadRoutesFromFile()

    def storeRouteToFile(self):
        return self.rouIO.storeRouteToFile()

    def loadPermitsFromFile(self):
        return self.perIO.loadPermitsFromFile()
    
    def storePermitToFile(self):
        return self.perIO.storePermitToFile()