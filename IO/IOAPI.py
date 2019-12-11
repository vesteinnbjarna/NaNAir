from IO.destinationIO import DestinationIO
from IO.voyageIO import VoyageIO
from IO.planeIO import PlaneIO
from IO.employeeIO import EmployeeIO
from IO.routeIO import RouteIO


class IOAPI ():

    def __init__(self):
        self.desIO = DestinationIO('IO/Data/Destinations.csv') # Hardcoded filenames - Only place to change the path is here
        self.voyIO = VoyageIO('IO/Data/Voyages.csv')
        self.plaIO = PlaneIO('IO/Data/Planes.csv')
        self.empIO = EmployeeIO('IO/Data/Crew.csv')
        self.rouIO = RouteIO('IO/Data/Routes.csv')
        #self.typIO = TypeIO('IO/Data/AircraftType.csv')

    def loadDestinationFromFile (self):
        return self.desIO.loadFile()
    
    def storeDestinationToFile(self,dest):
        return self.desIO.storeDestinationToFile(dest)

    def updateContactInfoInFile(self,line_index,row_index,updated_info):
        return self.desIO.updateContactInfoInFile(line_index,row_index,updated_info)

    def loadVoyagesFromFile (self):
        return self.voyIO.loadFile()
    
    def storeVoyageToFile(self,voyage):
        return self.voyIO.storeVoyageToFile(voyage)

    def updateVoyageInFile(self):
        return self.voyIO.updateVoyageInFile()

    def loadPlanesFromFile(self):
        return self.plaIO.loadFile()

    def storePlaneToFile(self,plane):
        return self.plaIO.storePlaneToFile(plane)

    def loadEmployeesFromFile(self):
        return self.empIO.loadFile()

    def storeEmployeeToFile(self,employee):
        return self.empIO.storeEmployeeToFile(employee)

    def updateEmployeeInFile(self,line_index,row_index,updated_info):
        return self.empIO.updateEmployeeInFile(line_index,row_index,updated_info)

    def loadRoutesFromFile(self):
        return self.rouIO.loadRoutesFromFile()

    def storeRouteToFile(self):
        return self.rouIO.storeRouteToFile()