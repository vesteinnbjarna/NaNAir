from UI.createEmployee import CreateEmployee
from UI.getEmployee import GetEmployee
from LL.LLAPI import LLAPI

#EMP
class EmployeeManagementUI():
    def __init__(self):
        self.createEmployee = CreateEmployee()
        self.getEmployee = GetEmployee()

    def renderMenu(self):
        #user_input = ""
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
                if createEmp == "Back":
                    continue
            elif user_input == "2":
                if self.getEmployee.get_user_input() == None:
                    return None                           #self.createEmployee.print_data_options()
            elif user_input == "3":
                pass
            elif user_input == "b":
                break
            else:
                continue

    

