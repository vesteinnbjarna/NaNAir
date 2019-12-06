#from IO.IOAPI import IOAPI

class EmployeeLL ():
    def __init__ (self, ioAPI):
        self.__ioAPI = ioAPI

    def createEmployee (self):
        self.__ioAPI.storeEmployeeToFile()
        pass
    
    def updateEmployee (self):
        self.__ioAPI.updateEmployeeInFile()
        pass

    def getEmployee (self):
        self.__ioAPI.loadEmployeesFromFile()
        pass

    
    

    