from IO.BaseClassIO import BaseClassIO
#from Model.employee import Employee

class EmployeeIO (BaseClassIO):
    def __init__(self,employee):
       self.employee = employee
    
    def loadEmployeesFromFile(self):
        pass

    def storeEmployeeToFile(self):
        self.employee.get_name()


        pass

    def updateEmployeeInFile(self):
        pass

    
        pass
