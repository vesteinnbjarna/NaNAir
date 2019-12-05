##ATH ÞETTA ERU BARA DRÖG ÚTFRÁ KLASARITINU



class IOAPI ():
    def __init__(self):
        pass
    

class DestinationIO ():

    def __init__(self):
        self.destinationFileName = 'destinations.csv'
    
    def loadDestinationFromFile(self):
        pass

    def storeDestinationToFile(self):
        pass

    def updateContactInfoInFile(self):
        pass


class VoyageIO ():
    def __init__(self):
         self.voyageFileName = 'voyages.csv'

    def loadVoyagesFromFile(self):
        pass

    def storeVoyageToFile(self):
        pass

    def updateVoyageInFile(self):
        pass

    
class PlaneIO ():
    def __init__(self):
        self.planeFileName = 'planes.csv'

    def loadPlanesFromFiles(self):
        pass

    def storePlaneToFile(self):
        pass

class EmployeeIO ():
    def __init__(self):
        self.employeeFileName = 'employees.csv'
    
    def loadEmployeesFromFile (self):
        pass

    def storeEmployeeToFile(self):
        pass

    def updateEmployeeInFile(self):
        pass



class RouteIO ():
    def __init__(self):
        self.routeFileName = 'routes.csv'


    def loadRoutesFromFile (self):
        pass

    def storeRouteToFile (self):
        pass


class PermitIO ():
    def __init__(self):
        self.permitFileName = 'permits.csv'

    def loadPermitsFromFile(self):
        pass

    def storePermitToFile(self):
        pass

print(dir(PermitIO))

print (IOAPI)