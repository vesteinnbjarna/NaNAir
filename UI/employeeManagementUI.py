from UI.createEmployee import CreateEmployee
from UI.getEmployee import GetEmployee
from UI.updateEmployee import UpdateEmployee
from LL.LLAPI import LLAPI

#EM
class EmployeeManagementUI():
    def __init__(self, llAPI_in):
        self.__llAPI_in = llAPI_in 
        self.createEmployee = CreateEmployee(self.__llAPI_in)
        self.getEmployee = GetEmployee(self.__llAPI_in)
        self.updateEmployee = UpdateEmployee(self.__llAPI_in)

    def renderMenu(self):
        ''' Method that gets user input and calls correct class. '''
        while True:
            print(''' ___________________________________________''')
            print('''|       NaN Air - Employee management       |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Create employee                       |''')
            print('''| (2) Get employee data                     |''')
            print('''| (3) Update employee                       |''')
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')

            user_input = input("Input: ")

            if user_input == "1":
                createEmp = self.createEmployee.get_employee_info()
                if createEmp == None:
                    return None
                if createEmp == "Back to emp_m":
                    continue
            elif user_input == "2":
                emp_user_input = self.getEmployee.get_user_input()
                if emp_user_input == None:
                    return None            
                if emp_user_input == "Back to emp_m":
                    continue
            elif user_input == "3":
                updateEmp = self.updateEmployee.get_input()
                if updateEmp == None:
                    return None
                if updateEmp == "Back to emp_m":
                    continue
            elif user_input == "b":
                break
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue
