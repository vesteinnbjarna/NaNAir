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

    def getDestinationHeader(self,list_of_destination):
        return self.destLL.getDestinationHeader(list_of_destination)


    def getDestinationValue(self,list_of_destination):
        return self.destLL.getDestinationValue(list_of_destination)


    def getDestinations(self):
        return self.destLL.getDestination()
    
    def createDestination(self,dest):
        return self.destLL.storeDestinationToFile(dest)

    def getDestinationsContactInfo(self):
        return self.destLL.getDestinationsContactInfo()

    def updateContactInfo(self,line_index,row_index,updated_info):
        return self.destLL.updateContactInfo(line_index,row_index, updated_info)

    def createVoyage(self,voyage):
        return self.voyLL.createVoyage(voyage)
    
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

    def getAvailablePlanes(self, date, totalTime):
        return self.plaLL.getAvailablePlanes(date,totalTime)

    def createEmployee(self,employee):
        return self.empLL.createEmployee(employee)
    
    def getEmployees(self):
        return self.empLL.getEmployees()

    def updateEmployee(self, line_index, row_index, updated_info):
       return self.empLL.updateEmployee(line_index, row_index, updated_info)

    def getEmployeeHeader(self,employee_list):
        return self.empLL.getEmployeeHeader(employee_list)

    def getEmployeeValue(self,employee_list):
        return self.empLL.getEmployeeValue(employee_list)

    def getPilotsOrFAs(self, empType):
        return self.empLL.getPilotsOrFAs(empType)
    
    def getSpecificEmployee(self, emp_id = ''):
        return self.empLL.getSpecificEmployee(emp_id)

    def getAvailabilityOfPilots(self, date, listType):
        return self.empLL.getAvailabiltyOfPilots(date, listType)

    def getAvailabiltyOfFAs(self, date, listType):
        return self.empLL.getAvailabiltyOfFAs(date, listType)
    
    def getAvailabilityOfAll(self, date, listType):
        return self.empLL.getAvailabilityOfAll(date, listType)
    
    def getChosenEmployee(self, id_list, emp_id):
        return self.empLL.getChosenEmployee(id_list, emp_id)
    def getVoyageHeader(self, voyage_list):
        return self.voyLL.getVoyageHeader(voyage_list)

    def getVoyageValue(self,voyage_list):
        return self.voyLL.getVoyageValue(voyage_list)
