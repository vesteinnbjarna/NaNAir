from LL.destinationLL import DestinationLL
from LL.employeeLL import EmployeeLL
from LL.planeLL import PlaneLL
from LL.voyageLL import VoyageLL
from IO.IOAPI import IOAPI

class LLAPI():
    pass

    def __init__(self):
        self.ioAPI = IOAPI()
        self.destLL = DestinationLL(self.ioAPI)
        self.voyLL = VoyageLL(self.ioAPI)
        self.plaLL = PlaneLL(self.ioAPI)
        self.empLL = EmployeeLL(self.ioAPI)

    def getDestinations(self):
        return self.destLL.getDestination()
    
    def getDestinationInIceland(self):
        return self.destLL.getDestinationInIceland()
    
    def updateContactInfo(self):
        return self.destLL.updateContactInfo()

    def createVoyage(self):
        return self.voyLL.createVoyage()
    
    def getVoyages(self):
        return self.voyLL.getVoyages()

    def updateVoyage(self):
        return self.voyLL.updateVoyage()
    
    def createPlane(self):
        return self.plaLL.createPlane()

    def getPlanes(self):
        return self.plaLL.getPlanes()

    def createEmployee(self):
        return self.empLL.createEmployee()
    
    def getEmployee(self):
        return self.empLL.getEmployee()

    def updateEmployee(self):
        return self.empLL.updateEmployee()

    



    