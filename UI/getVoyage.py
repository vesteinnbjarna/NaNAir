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
        pass
    
    def get_list_of_voyages(self):
        print()
        print(''' ___________________________________________''')
        print('''|                  NaN Air                  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) List of voyages for a specific date   |''')
        print('''| (2) List of voyages for a specific week   |''')
        print('''|                                           |''')
        print('''| press 'b' for back                        |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')       
        print()
        user_input = input("Input: ")
        print()
        if user_input == "1":
            self.get_date = input("Enter date (mm/dd/yy): ")
            self.print_choosen_list()
            #Senda date áfram í data layer 
        elif user_input == "2":
            self.get_week = input("Enter week (1-52): ") 
            self.print_choosen_list()
            #Senda week áfram í data layer
        elif user_input == "b":
            self.get_list()
        else:
            self.get_list_of_voyages()


    def print_choosen_list(self):
        print()
        print("#Prentast út viðeigandi listi sem data layer er búinn að senda til baka")
        print()
        print(''' ___________________________________________''')
        print('''|                  NaN Air                  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) List of destinations                  |''')
        print('''| (2) List of voyages                       |''')
        print('''|                                           |''')
        print('''| (3) Go back to home page                  |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')       
        print()
        user_input = input("Input: ")
        print()
        if user_input == "1":
            self.get_list_of_destinations()
        elif user_input == "2":
            self.get_list_of_voyages()
        elif user_input == "3":
            return None
