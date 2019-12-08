#from IO.IOAPI import IOAPI

class EmployeeLL ():
    def __init__ (self, ioAPI):
        self.__ioAPI = ioAPI

    def createEmployee (self,employee):
        self.__ioAPI.storeEmployeeToFile(employee)
        
    
    def updateEmployee (self):
        self.__ioAPI.updateEmployeeInFile()
        pass

    def getEmployee (self):
        return self.__ioAPI.loadEmployeesFromFile()

    def getPilotsOrFAs(self,empType, sorting):
        list_of_employees = self.__ioAPI.loadEmployeesFromFile()
        listOfPilots = []
        listOfFAs = []
        if empType == "Pilot":
            for line in list_of_employees:
                for key,val in line.items():
                    if key == "role":
                        if val == empType:
                            listOfPilots.append(line)
            return listOfPilots
        elif empType == "Cabincrew":
            for line in list_of_employees:
                for key,val in line.items():
                    if key == "role":
                        if val == empType:
                            listOfFAs.append(line)
            return listOfFAs