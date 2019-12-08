from IO.BaseClassIO import BaseClassIO
from Model.employee import Employee

class EmployeeIO (BaseClassIO):
    def __init__(self,filename):
       self.filename = filename
       
    
    def loadEmployeesFromFile(self):
        pass

    def storeEmployeeToFile(self,employee):
        next_id = self.getNextID()
        #Employee.assign_id(next_id)

        ssn = Employee.get_ssn(employee)
        name = Employee.get_name(employee)
        role = Employee.get_role(employee)
        #rank = Employee.get_rank(employee)
        address = Employee.get_address(employee)
        phone_no = Employee.get_phonenumber(employee)
        email = Employee.get_email(employee)
        emp_id = next_id   #str(Employee.get_id(employee))
        emp_license = Employee.get_license(employee)

        employee_info = '\n{},{},{},{},{},{},{},{}'.format(emp_id,ssn,name,role,emp_license,address,phone_no,email)
        print(employee_info)
        
        
        
        
        
        
        with open(self.filename,'a') as f:
            f.write(employee_info)
        



    def updateEmployeeInFile(self):
        pass

    
        pass
