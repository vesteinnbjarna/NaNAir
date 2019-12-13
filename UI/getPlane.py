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
                plane_list = self.llAPI_in.getPlanes()
                self.print_list(plane_list)
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

    def print_list(self, plane_list):
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
        input("Press enter to go back")

    def print_list_status(self, plane_list):
        counter = 0
        for line in plane_list:
            if counter < 1:
                for key in line.keys():
                    print("{:24}".format(key), end=" ")
                counter += 1
        print()
        print("__"*55)
        print()
        for line in plane_list:
            for key,val in line.items():
                print("{:24}".format(val), end=" ")
            print()
        print()
        input("Press enter to go back")



############# GET PLANE STATUS ##################

    def get_plane_status(self):
        dateTime = self.get_date_input()
        planeStatus = self.llAPI_in.getPlaneStatus(dateTime)
        self.print_list_status(planeStatus)
        return None

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
                year = int(input("Enter year (yyyy): "))
                month = int(input("Enter month (mm): "))
                day = int(input("Enter day (dd): "))
                time = input("Enter time (hh:mm): ")
                invalid_input = False
            except ValueError:
                print(''' _________________________''')
                print('''|Invalid input! try again.|''')
                print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')                
                continue
            print("\n\n")
            try:
                hours = time[:2]
                minutes = time[3:]
                if hours[0] == '0':
                    hours = int(hours[1])
                else:
                    hours = int(hours)
                if minutes[0] == '0':
                    minutes = int(minutes[1])
                else:
                    minutes = int(minutes)
                self.dateTime = datetime.datetime(year,month,day,hours,minutes)
                return self.dateTime
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