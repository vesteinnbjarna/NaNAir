#from IO.IOAPI import IOAPI

class EmployeeLL ():
    def __init__ (self, ioAPI):
        self.__ioAPI = ioAPI

    def createEmployee (self,employee):
        self.__ioAPI.storeEmployeeToFile(employee)
        
    
    def updateEmployee (self):
        self.__ioAPI.updateEmployeeInFile()
        pass

    def getEmployees(self):
        return self.__ioAPI.loadEmployeesFromFile()

    def getPilotsOrFAs(self,empType, sorting):
        list_of_employees = self.__ioAPI.loadEmployeesFromFile()
        listOfPilots = []
        listOfFAs = []
        if empType == "Pilot":
            for line in list_of_employees:
                for key,val in line.items():
                    if key == "Role":
                        if val == empType:
                            listOfPilots.append(line)
            return listOfPilots
        elif empType == "Cabincrew":
            for line in list_of_employees:
                for key,val in line.items():
                    if key == "Role":
                        if val == empType:
                            listOfFAs.append(line)
            return listOfFAs

    def getSpecificEmployee(self, id):
        list_of_employees = self.__ioAPI.loadEmployeesFromFile()
        for line in list_of_employees:
            for key,val in line.items():
                if key == "ID":
                    if val == id:
                        return line

