from UI.employeeManagementUI import EmployeeManagementUI
from UI.voyageManagementUI import VoyageManagementUI
from UI.planeManagementUI import PlaneManagementUI



class MainPage():
    def __init__(self):
        self.__employeeManagement = EmployeeManagementUI()
        self.__voyageManagement = VoyageManagementUI()
        self.__planeManagement = PlaneManagementUI()
        self.renderMenu()

    def renderMenu(self):
        user_input = "1"
        while user_input == "1" or user_input == "2" or user_input == "3":
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Employee Management                   |''')
            print('''| (2) Voyage Management                     |''')
            print('''| (3) Plane Management                      |''')
            print('''|                                           |''')
            print('''| (press "b" for back and "q" to quit)      |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input()
            if user_input == "1":
                self.__employeeManagement.renderMenu()
            elif user_input == "2":
                self.__voyageManagement.renderMenu()
            elif user_input == "3":
                self.__planeManagement.renderMenu()

a = MainPage()
a.renderMenu()