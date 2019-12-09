from UI.createVoyage import CreateVoyage
from UI.getVoyage import GetVoyage
from UI.updateVoyage import UpdateVoyage
from LL.LLAPI import LLAPI
class VoyageManagementUI():
    def __init__(self, llAPI_in):
        self.llAPI_in = llAPI_in
        self.createVoyage = CreateVoyage(llAPI_in)
        self.getVoyage = GetVoyage(llAPI_in)
        self.updateVoyage = UpdateVoyage(llAPI_in)

    def renderMenu(self):
        while True:
            print(''' ___________________________________________''')
            print('''|        NaN Air - Voyage management        |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Create voyage                         |''')
            print('''| (2) Get voyage data                       |''')
            print('''| (3) Update voyage                         |''')
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            if user_input == "1":
                createVoy = self.createVoyage.get_input()
                if createVoy == None:
                    return None
                elif createVoy == "Back to voy_m":
                    continue
            elif user_input == "2":
                getVoy = self.getVoyage.get_list()
                if getVoy == None:
                    return None
                elif getVoy == "Back to voy_m":
                    continue
            elif user_input == "3":
                updateVoy = self.updateVoyage.get_input()
                if updateVoy == None:
                    return None
                elif updateVoy == "Back to voy_m":
                    continue
            elif user_input == "b":
                return None
            else:
                continue




