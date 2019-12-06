from UI.createEmployee import CreateEmployee
from UI.getEmployee import GetEmployee
#from UI.updateEmployee import UpdateEmployee
#from LL.LLAPI import LLAPI

#EMP
class EmployeeManagementUI():
    def __init__(self, llAPI_in):
        self.__llAPI_in = llAPI_in 
        self.createEmployee = CreateEmployee(self.__llAPI_in)
        self.getEmployee = GetEmployee(self.__llAPI_in)
        #self.updateEmployee = UpdateEmployee(self.__llAPI_in)

    def renderMenu(self):
<<<<<<< HEAD
=======
        #user_input = ""
>>>>>>> c15cbd9f8333901fa074822a97eb4da3a1cf9988
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
<<<<<<< HEAD
                if self.createEmployee.get_employee_info() == None:
                    continue
               #if self.get_employee_info() == None:
            elif user_input == "2":
                if self.getEmployee.get_user_input() == None:
                    continue            #self.createEmployee.print_data_options()
=======
                createEmp = self.createEmployee.get_employee_info()
                if createEmp == None:
                    return None
                if createEmp == "Back":
                    continue
            elif user_input == "2":
                if self.getEmployee.get_user_input() == None:
                    return None                           #self.createEmployee.print_data_options()
>>>>>>> c15cbd9f8333901fa074822a97eb4da3a1cf9988
            elif user_input == "3":
                pass
            elif user_input == "b":
                break
            else:
<<<<<<< HEAD
                continue
=======
                continue

    

>>>>>>> c15cbd9f8333901fa074822a97eb4da3a1cf9988
