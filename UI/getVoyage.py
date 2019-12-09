from Model.voyage import Voyage

class GetVoyage():
    def __init__(self, llAPI_in):
        self.llAPI_in = llAPI_in

    def get_list(self):
        while True:
            print()
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) List of destinations                  |''')
            print('''| (2) List of voyages                       |''')
            print('''|                                           |''')
            print('''| press 'b' for back                        |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')       
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                self.get_list_of_destinations()
            elif user_input == "2":
                self.get_list_of_voyages()
            elif user_input == "b":
                return "Back to voy_m"
            else:
                continue
    
    def get_list_of_destinations(self):
        #Prentast út listi af destinations sem data layer er búinn að senda til baka
        line_index = 0
        destination_list = self.llAPI_in.getDestinations()
        counter = 0
        for line in destination_list:
            if counter < 1:
                for key in line.keys():
                    print(key, end="\t")
                counter += 1
            else:
                print()
                break
        for line in destination_list:
            for key,val in line.items():
                print(val, end="\t")
                line_index += 1
            print()
        print()
        user_input = input("Press enter to go back")
    
    def get_list_of_voyages(self):
        while True:
            print()
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) List of all voyages                   |''')
            print('''| (2) List of voyages for a specific date   |''')
            print('''| (3) List of voyages for a specific week   |''')
            print('''|                                           |''')
            print('''| press 'b' for back                        |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')       
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                self.print_choosen_list()
            elif user_input == "2":
                self.get_date = input("Enter date (mm/dd/yy): ")
                self.print_choosen_list()
                #Senda date áfram í data layer 
            elif user_input == "3":
                self.get_week = input("Enter week (1-52): ") 
                self.print_choosen_list()
                #Senda week áfram í data layer
            elif user_input == "b":
                self.get_list()
            else:
                continue


    def print_choosen_list(self):
        line_index = 0
        voyage_list = self.llAPI_in.getVoyages()
        counter = 0
        for line in voyage_list:
            if counter < 1:
                for key in line.keys():
                    print(key, end="\t")
                counter += 1
            else:
                print()
                break
        for line in voyage_list:
            for key,val in line.items():
                print(val, end="\t")
                line_index += 1
            print()
        print()
        user_input = input("Press enter to go back")


    
