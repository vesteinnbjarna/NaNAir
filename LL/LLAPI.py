from LL.destinationLL import DestinationLL
from LL.employeeLL import EmployeeLL
from LL.planeLL import PlaneLL
from LL.voyageLL import VoyageLL
from IO.IOAPI import IOAPI

class LLAPI():
    def __init__(self):
        self.__ioAPI = IOAPI()
        self.destLL = DestinationLL(self.__ioAPI)
        self.voyLL = VoyageLL(self.__ioAPI)
        self.plaLL = PlaneLL(self.__ioAPI)
        self.empLL = EmployeeLL(self.__ioAPI)

    def getDestinations(self):
        return self.destLL.getDestination()
    
    def createDestination(self,dest):
        return self.destLL.storeDestinationToFile(dest)
    
    def updateContactInfo(self):
        return self.destLL.updateContactInfo()

    def createVoyage(self):
        return self.voyLL.createVoyage()
    
    def getVoyages(self):
        return self.voyLL.getVoyages()

    def getVoyagesWeek(self, first_day_of_week):
        return self.voyLL.getVoyagesWeek(first_day_of_week)

    def getVoyagesDay(self,date):
        return self.voyLL.getVoyagesDay(date)

    def updateVoyage(self):
        return self.voyLL.updateVoyage()
    
    def createPlane(self,plane):
        return self.plaLL.createPlane(plane)

    def getPlanes(self):
        return self.plaLL.getPlanes()

    def createEmployee(self,employee):
        return self.empLL.createEmployee(employee)
    
    def getEmployees(self):
        return self.empLL.getEmployees()

    def updateEmployee(self):
        return self.empLL.updateEmployee()

    def getPilotsOrFAs(self, empType, sorting = ''):
        return self.empLL.getPilotsOrFAs(empType, sorting)