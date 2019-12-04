class EmployeeManagement():
    def renderMenu(self):
        user_input = "1"
        while user_input == "1" or user_input == "2" or user_input == "3":
            print(''' -------------------------------------------''')
            print('''|                  NaN Air                  |''')
            print(''' ------------------------------------------- ''')
            print('''| (1) Create employee                       |''')
            print('''| (2) Get employee data                     |''')
            print('''| (3) Update employee                       |''')
            print('''|                                           |''')
            print('''| (press "b" for back and "q" to quit)      |''')
            print(''' -------------------------------------------''')
            user_input = input("Input: ")

class PlaneManagement():
    def renderMenu(self):
        user_input = "1"
        while user_input == "1" or user_input == "2":
            print(''' -------------------------------------------''')
            print('''|                  NaN Air                  |''')
            print(''' ------------------------------------------- ''')
            print('''| (1) Create plane                          |''')
            print('''| (2) Get list of planes                    |''')
            print('''|                                           |''')
            print('''| (press "b" for back and "q" to quit)      |''')
            print(''' -------------------------------------------''')
            user_input = input("Input: ")
            

class VoyageManagement():
    def renderMenu(self):
        user_input = "1"
        while user_input == "1" or user_input == "2":
            print(''' -------------------------------------------''')
            print('''|                  NaN Air                  |''')
            print(''' ------------------------------------------- ''')
            print('''| (1) Create destination                    |''')
            print('''| (2) Create voyage                         |''')
            print('''|                                           |''')
            print('''| (press "b" for back and "q" to quit)      |''')
            print(''' -------------------------------------------''')
            user_input = input("Input: ")

class MainPage():
    def __init__(self):
        self.__employeeManagement = EmployeeManagement()
        self.__voyageManagement = VoyageManagement()
        self.__planeManagement = PlaneManagement()

    def renderMenu(self):
        user_input = "1"
        while user_input == "1" or user_input == "2" or user_input == "3":
            print(''' -------------------------------------------''')
            print('''|                  NaN Air                  |''')
            print(''' ------------------------------------------- ''')
            print('''| (1) Employee Management                   |''')
            print('''| (2) Voyage Management                     |''')
            print('''| (3) Plane Management                      |''')
            print('''|                                           |''')
            print('''| (press "b" for back and "q" to quit)      |''')
            print(''' -------------------------------------------''')
            user_input = input("Input: ")
            if user_input == "1":
                self.__employeeManagement.renderMenu()
            elif user_input == "2":
                self.__voyageManagement.renderMenu()
            elif user_input == "3":
                self.__planeManagement.renderMenu()
            

mainPage = MainPage()
mainPage.renderMenu()

