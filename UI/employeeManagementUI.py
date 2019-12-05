from UI.createEmployee import CreateEmployee
from UI.getEmployee import GetEmployee

class EmployeeManagementUI():
    def __init__(self):
        self.createEmployee = CreateEmployee()
        self.getEmployee = GetEmployee()

    def renderMenu(self):
        #user_input = ""
        #while True:
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
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                if self.createEmployee.get_employee_info() == None:
                    self.renderMenu()
               #if self.get_employee_info() == None:
            elif user_input == "2":
                if self.getEmployee.get_user_input() == None:
                    self.renderMenu()            #self.createEmployee.print_data_options()
            elif user_input == "3":
                pass
            elif user_input == "b":
                return None
            else:
                self.renderMenu()   #continue