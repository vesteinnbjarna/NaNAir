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
        
        

    
    

    