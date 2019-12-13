from Model.plane import Plane
import datetime

class GetPlane():
    def __init__(self, llAPI_in):
        self.llAPI_in  = llAPI_in

    def choose_list(self):
        user_input = "1"
        # Runs until valid input is chosen or back
        while True:
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')  
            print('''| (1) Get list of all NaN-Air planes        |''')
            print('''| (2) Get list of plane status              |''')
            print('''|     by date and time                      |''')
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            print() 
            if user_input == "1":
                self.print_list()
            elif user_input == "2":
                self.get_plane_status()
            elif user_input == "b":
                return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue

    def print_list(self):
        plane_list = self.llAPI_in.getPlanes()
        counter = 0
        for line in plane_list:
            if counter < 1:
                for key in line.keys():
                    print("{:20}".format(key), end=" ")
                counter += 1
        print()
        print("__"*20)
        print()
        for line in plane_list:
            for key,val in line.items():
                print("{:20}".format(val), end=" ")
            print()
        print()
        user_input = input("Press enter to go back")



############# GET PLANE STATUS ##################

    def get_plane_status(self):
        self.get_list()
        plane_status = self.llAPI_in.getPlaneStatus(self.chosen_plane, self.date, self.time)


    def get_list(self):
        invalid_input = True
        while invalid_input == True:
            print()
            plane_list = []
            plane_dict = self.llAPI_in.getPlanes()
            print("     {:15}{:15}".format("Plane ID", "Plane Type"))
            print("__"*20)
            print()
            counter = 1
            for line in plane_dict:
                print("({})".format(counter), end=" ")
                for key,val in line.items():
                    print("{:15}".format(val), end=" ")
                    if key == 'planeInsignia':
                        plane_list.append(val)
                counter += 1
                print()
            print()
            user_input = input("Choose plane: ")

            #Check if input is valid
            if len(user_input) == 1:
                try:
                    user_input = int(user_input)
                    if user_input in range(1, len(plane_list) + 1):
                        invalid_input = False
                except ValueError:
                    print("Invalid input!")
                    print()
                    input("Press enter to try again :-) ")
                    continue
            else:
                print("Invalid input!")
                print()
                input("Press enter to try again :-) ")  
                continue             

        for index in range(len(plane_list) + 1):
            if index == user_input:
                self.chosen_plane = plane_list[index - 1]
        print()
        print("Chosen plane: {}".format(self.chosen_plane))
        self.get_date_input()




    def get_date_input(self):
        ''' Method that gets date input and check if valid,
            and returns date in datetime format. '''
        invalid_input = True
        while invalid_input == True:
            try:
                self.year = int(input("Enter year (yyyy): "))
                self.month = int(input("Enter month (mm): "))
                self.day = int(input("Enter day (dd): "))
                self.time = input("Enter time (hh:mm): ")
                invalid_input = False
            except ValueError:
                print(''' _________________________''')
                print('''|Invalid input! try again.|''')
                print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')                
                continue
            print("\n\n")
            try:
                self.date = datetime.date(self.year, self.month, self.day)
                return self.date
            except ValueError:
                print(''' _________________________''')
                print('''|Invalid date! try again.|''')
                print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')                
                continue

        while True:
            self.time = input("Enter time (hh:mm): ")
            try:
                hours_int = int(self.time[:2])
                minutes_int = int(self.time[3:])
            except ValueError:
                print()
                print(" Invalid time, must be integer!")
                print()
                continue 