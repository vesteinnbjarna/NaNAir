from UI.employeeManagementUI import EmployeeManagementUI
from UI.planeManagementUI import PlaneManagementUI
from UI.voyageManagementUI import VoyageManagementUI
from LL.LLAPI import LLAPI

class MainPageUI():
    def __init__(self):
        self.__employeeManagement = EmployeeManagementUI()
        self.__voyageManagement = VoyageManagementUI()
        self.__planeManagement = PlaneManagementUI()

    def renderMenu(self):
        user_input = ""
        while user_input != "q":
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Employee Management                   |''')
            print('''| (2) Voyage Management                     |''')
            print('''| (3) Plane Management                      |''')
            print('''|                                           |''')
            print('''| (press "q" to quit)                       |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            if user_input == "1":
                self.__employeeManagement.renderMenu()
            elif user_input == "2":
                self.__voyageManagement.renderMenu()
            elif user_input == "3":
                self.__planeManagement.renderMenu()
            else:
                continue


a = MainPageUI()
a.renderMenu()

