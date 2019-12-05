from Model.voyage import Voyage

class VoyageManagementUI():
    def renderMenu(self):
        #user_input = "1"
        #while user_input == "1" or user_input == "2":
            print(''' ___________________________________________''')
            print('''|        NaN Air - Voyage management        |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print('''| (1) Create voyage                         |''')
            print('''| (2) Get voyage data                       |''')
            print('''| (3) Update voyage                         |''')
            print('''|                                           |''')
            print('''| (4) Go back to home page                  |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input()
            if user_input == "1":
                if self.get_input() == None:
                    return None
            elif user_input == "2":
                pass
            elif user_input == "3":
                pass
            elif user_input == "4":
                return None




