from Model.plane import Plane

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
            print('''| (2) Get list of planes status             |''')
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
                self.get_list()
            elif user_input == "b":
                return None
            else:
                continue

    def print_list(self):
        line_index = 0
        plane_list = self.llAPI_in.getPlanes()
        counter = 0
        for line in plane_list:
            if counter < 1:
                for key in line.keys():
                    print(key, end="\t")
                counter += 1
        print()
        print("___________________________________________")
        print()
        for line in plane_list:
            for key,val in line.items():
                print(val, end=" "*10)
                line_index += 1
            print()
        print()
        user_input = input("Press enter to go back")


    def get_list(self):
        print()
        self.date = input("Enter date (mm/dd/yy): ")
        self.time = input("Enter time (hh:mm): ")
        print()
        # senda svo áfram date og time í data layer
        