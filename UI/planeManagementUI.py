from UI.createPlane import CreatePlane
from UI.getPlane import GetPlane

class PlaneManagementUI():

    def __init__(self, llAPI_in):
        self.__llAPI_in = llAPI_in 
        self.createPlane = CreatePlane()
        self.getPlane = GetPlane()


    def renderMenu(self):
<<<<<<< HEAD
        user_input = "1"
        # Runs until valid input is chosen or back
=======
        #user_input = "1"
>>>>>>> c15cbd9f8333901fa074822a97eb4da3a1cf9988
        while True:
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| ''')
            print('''|                                           |''')   
            print('''| (1) Create plane                          |''')
            print('''| (2) Get list of planes                    |''')
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            #print()
            user_input = input("Input: ")
            #print()
            if user_input == "1":
                if self.createPlane.get_plane_info() == None: # Ef fallið get_plane_info skilar None þá vill hann fara í main page
                    return None
            elif user_input == "2":
                if self.getPlane.get_list() == None:
                    return None
            elif user_input == "b":
                return None
            else:
                continue

