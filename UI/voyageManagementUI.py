from UI.createVoyage import CreateVoyage
from UI.getVoyage import GetVoyage
from UI.updateVoyage import UpdateVoyage

class VoyageManagementUI():
    def __init__(self):
        self.createVoyage = CreateVoyage()
        self.getVoyage = GetVoyage()
        self.updateVoyage = UpdateVoyage()

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
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            if user_input == "1":
                if self.createVoyage.get_input() == None:
                    self.renderMenu()
            elif user_input == "2":
                if self.getVoyage.get_list() == None:
                    self.renderMenu()
            elif user_input == "3":
                if self.updateVoyage.get_input() == None:
                    self.renderMenu()
            elif user_input == "b":
                return None




