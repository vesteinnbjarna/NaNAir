from Model.Plane import Plane

class CreatePlane():
    def __init__(self, llAPI_in):
        self.llAPI_in = llAPI_in

    def get_plane_info(self):
        print(' __________________________________________')
        print("| NaN Air - Enter plane information        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
        self.registration = input("Enter aircraft registration: ")
        self.plane_type = input("Enter aircraft type: ")
        self.manufacturer = input("Enter aircraft manufacturer: ")
        self.seats = input("Enter number of seats: ")
        self.display_info()

    def display_info(self):
        while True:
            print(''' ___________________________________________''')
            print('''|        NaN Air - Review information       |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Aircraft registration: {:19}|'''.format(self.registration))
            print('''| Aircraft type: {:27}|'''.format(self.plane_type))
            print('''| Aircraft manufacturer: {:19}|'''.format(self.manufacturer))
            print('''| Number of seats: {:25}|'''.format(self.seats))
            print('''|                                           |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Confirm                               |''')
            print('''| (2) Edit                                  |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            if user_input == "1":
                if self.create_plane():
                    self.print_confirmation()   # Ef fallið get_plane_info skilar None þá vill hann fara í main page
                    return None
            elif user_input == "2":
                self.edit_info()
            else:
                continue
            

    def edit_info(self):
        print(''' ___________________________________________''')
        print('''|        NaN Air - Edit information         |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Aircraft registration: {:15}|'''.format(self.registration))
        print('''| (2) Aircraft type: {:23}|'''.format(self.plane_type))
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
            self.plane_type = input("Enter aircraft type: ")
        elif user_input == "3":
            self.manufacturer = input("Enter aircraft manufacturer: ")
        elif user_input == "4":
            self.seats = input("Enter number of seats: ")
        elif user_input == "b":
            self.display_info()
        self.display_info()


    def create_plane(self):
        self.plane = Plane(self.registration, self.plane_type, self.manufacturer, self.seats)
        self.llAPI_in.createPlane(self.plane)
        return self.plane

    def print_confirmation(self):
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


