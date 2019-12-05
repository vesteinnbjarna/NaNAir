from IO.destinationIO import DestinationIO
from IO.voyageIO import VoyageIO
from IO.planeIO import PlaneIO
from IO.employeeIO import EmployeeIO
from IO.routeIO import RouteIO
from IO.permitIO import PermitIO

class IOAPI ():

    def __init__(self):
        self.desIO = DestinationIO()
        self.voyIO = VoyageIO()
        self.plaIO = PlaneIO()
        self.empIO = EmployeeIO()
        self.rouIO = RouteIO()
        self.perIO = PermitIO()
        

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
        return self.empIO.loadEmployeesFromFile()

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