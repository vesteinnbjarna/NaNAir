from Model.Plane import Plane
from Model.PlaneType import PlaneType

class CreatePlane():
    def __init__(self, llAPI_in):
        self.llAPI_in = llAPI_in

    def get_plane_info(self):
        print(' __________________________________________')
        print("| NaN Air - Enter plane information        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
        self.plane_type = self.choosePlaneType()
        self.registration = input("Enter aircraft registration: ")
<<<<<<< HEAD
        self.planeType = input("Enter aircraft type: ")
        self.manufacturer = input("Enter aircraft manufacturer: ")
        self.seats = input("Enter number of seats: ")
=======
        self.plane = Plane(self.registration,self.plane_type)
>>>>>>> a1dab497258b4bd279a0de7f825271fa6b140d80
        self.display_info()
        return None

    def choosePlaneType(self):
        planeType_list = self.llAPI_in.getPlaneType_list()
        while True:
            print()
            print('{}    {:>15} {:>10}'.format('ID','Plane Type', 'Manufacturer'))
            print(35 * '_')
            print()
            counter = 1
            for planeType in planeType_list:
                print('({})  {:>15} {:>10}'.format(counter,planeType['planeTypeId'],planeType['manufacturer']))
                counter += 1
            print()
            print('({})  {:>15}'.format(counter, 'Other'))
            print()
            print("Choose aircraft type")
            user_choice = input("Enter ID: ")
            print()
            valid_input = False
            while not valid_input:
                try:
                    user_choice = int(user_choice)
                    valid_input = True
                except ValueError:
                    print('Invalid input! Please enter a valid ID.')
                    user_choice = input("Choose aircraft type: ")
            if 0 < user_choice < counter:
                chosenPlaneType_odict = planeType_list[user_choice - 1]
                chosenPlaneType_obj = PlaneType(chosenPlaneType_odict['planeTypeId'], chosenPlaneType_odict['manufacturer'],\
                    chosenPlaneType_odict['model'],chosenPlaneType_odict['capacity'])
                return chosenPlaneType_obj
            elif user_choice == counter:
                pass
            else:
                print("Not a valid ID! Press enter to try again.")
                input()
                continue

    def display_info(self):
        while True:
            print(''' ___________________________________________''')
            print('''|        NaN Air - Review information       |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Aircraft registration: {:19}|'''.format(self.registration))
<<<<<<< HEAD
            print('''| Aircraft type: {:27}|'''.format(self.planeType))
            print('''| Aircraft manufacturer: {:19}|'''.format(self.manufacturer))
            print('''| Number of seats: {:25}|'''.format(self.seats))
=======
            print('''| Aircraft type: {:27}|'''.format(self.plane_type.plane_type))
            print('''| Aircraft manufacturer: {:19}|'''.format(self.plane_type.manufacturer))
>>>>>>> a1dab497258b4bd279a0de7f825271fa6b140d80
            print('''|                                           |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Confirm                               |''')
            print('''| (2) Cancel                                |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            if user_input == "1":
                self.create_plane()
                self.print_confirmation()   # Ef fallið get_plane_info skilar None þá vill hann fara í main page
                return None
            elif user_input == "2":
                return None
            else:
                continue
<<<<<<< HEAD
            

    def edit_info(self):
        while True:
            print(''' ___________________________________________''')
            print('''|        NaN Air - Edit information         |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Aircraft registration: {:15}|'''.format(self.registration))
            print('''| (2) Aircraft type: {:23}|'''.format(self.planeType))
            print('''| (3) Aircraft manufacturer: {:15}|'''.format(self.manufacturer))
            print('''| (4) Number of seats: {:21}|'''.format(self.seats))
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Edit selection: ")
            if user_input == "1":
                self.registration = input("Enter aircraft registration: ")
            elif user_input == "2":
                self.planeType = input("Enter aircraft type: ")
            elif user_input == "3":
                self.manufacturer = input("Enter aircraft manufacturer: ")
            elif user_input == "4":
                self.seats = input("Enter number of seats: ")
            elif user_input == "b":
                self.display_info()
            #self.display_info()
            else:
                continue


    def create_plane(self):
        self.plane = PlaneType(self.registration, self.planeType, self.manufacturer, self.seats)
=======

    def create_plane(self):
>>>>>>> a1dab497258b4bd279a0de7f825271fa6b140d80
        self.llAPI_in.createPlane(self.plane)
        return None

    def print_confirmation(self):
<<<<<<< HEAD
        while true:
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Plane successfullly created!              |''')
            print('''|                                           |''')
            print('''| (1) Create another plane                  |''')
            print('''| (2) Go back to home page                  |''')
            print('''|                                           |''')
            print('''|___________________________________________|''')
            print()
            user_input = input("Input: ")
            if user_input == "1":
                self.get_plane_info()
            elif user_input == "2":
                return None     # Skil None þá vill hann fara í main page
            else:
                continue


=======
        print(''' ___________________________________________''')
        print('''|                  NaN Air                  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| Plane successfullly created!              |''')
        print('''|                                           |''')
        print('''| (1) Create another plane                  |''')
        print('''| (2) Go back to home page                  |''')
        print('''|                                           |''')
        print('''|___________________________________________|''')
        print()
        user_input = input("Input: ")
        if user_input == "1":
            self.get_plane_info()
        elif user_input == "2":
            return None     # Skil None þá vill hann fara í main page
>>>>>>> a1dab497258b4bd279a0de7f825271fa6b140d80
