from Model.voyage import Voyage
import datetime

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
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue
    
    def get_list_of_destinations(self):
        #Prentast út listi af destinations sem data layer er búinn að senda til baka
        #line_index = 0
        destination_list = self.llAPI_in.getDestinations()
        dest_list_header = self.llAPI_in.getDestinationHeader(destination_list)
        dest_list_value = self.llAPI_in.getDestinationValue(destination_list)
        counter = 0
        for line in dest_list_header:
            if counter < 1:
                print("{:<5}{:<15}{:<15}{:<20}{:<12}{:<12}{:<22}{:<18}".format(
                    dest_list_header[0],dest_list_header[1],dest_list_header[2],dest_list_header[3],dest_list_header[4],
                    dest_list_header[5],dest_list_header[6],dest_list_header[7]))
                counter += 1
                print("__"*60)
                print()
            else:
                #print()
                break
        for line in dest_list_value:
            print("{:<5}{:<15}{:<15}{:<20}{:<12}{:<12}{:<22}{:<18}".format(
                line[0],line[1],line[2],line[3],line[4],
                line[5],line[6],line[7]))
            print()
        print()
        input("Press enter to continue!")
    
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
                voyage_list = self.llAPI_in.getVoyages()
                #print(voyage_list)
                self.print_chosen_list(voyage_list)
            elif user_input == "2":
                self.date = self.get_date_input()
                voyage_list_day = self.llAPI_in.getVoyagesDay(self.date)
                self.print_chosen_list(voyage_list_day)
                #Senda date áfram í data layer 
            elif user_input == "3":
                print()
                print(''' ___________________________________________''')
                print('''|             First day of week             |''')
                print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
                print()
                self.date = self.date = self.get_date_input()
                voyage_list_week = self.llAPI_in.getVoyagesWeek(self.date)
                self.print_chosen_list(voyage_list_week)
                #Senda week áfram í data layer
            elif user_input == "b":
                return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue


    def print_chosen_list(self, list_of_voyages):
        
        h_list = self.llAPI_in.getVoyageHeader(list_of_voyages)
        v_list = self.llAPI_in.getVoyageValue(list_of_voyages)
        print()
        if v_list!= None and h_list != None:
            if len(h_list) == 13:
                print("{:<5}{:<10}{:<10}{:<15}{:<25}{:<25}{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}{:<8}".format(
                    h_list[0],h_list[1],h_list[2],h_list[3],h_list[4],
                    h_list[5],h_list[6],h_list[7],h_list[8],h_list[9],h_list[10],h_list[11],h_list[12]))
            
                print("__"*90, "\n")

                for line in v_list:
                    print("{:<5}{:<10}{:<10}{:<15}{:<25}{:<25}{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}{:<8}".format(
                    line[0],line[1],line[2],line[3],line[4],
                    line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12]))
                print("\n\n")
            else:
                print("{:<5}{:<10}{:<10}{:<15}{:<25}{:<25}{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(
                h_list[0],h_list[1],h_list[2],h_list[3],h_list[4],
                h_list[5],h_list[6],h_list[7],h_list[8],h_list[9],h_list[10],h_list[11]))

                for line in v_list:
                    print("{:<5}{:<10}{:<10}{:<15}{:<25}{:<25}{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(
                    line[0],line[1],line[2],line[3],line[4],
                    line[5],line[6],line[7],line[8],line[9],line[10],line[11]))

        else:
            print('No voyages on {}'.format(self.date))
        input("Press enter to continue")

    def get_date_input(self):
        ''' Method that gets date input and check if valid,
        and returns date in datetime format. '''
        while True:
            try:
                self.year = int(input("Enter year (yyyy): "))
                self.month = int(input("Enter month (mm): "))
                self.day = int(input("Enter day (dd): "))
            except ValueError:
                print(''' ___________________________''')
                print('''| Invalid input! try again. |''')
                print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')                
                continue
            print("\n\n")
            try:
                hours = 0
                minutes = 0
                self.date = datetime.datetime(self.year, self.month, self.day, hours, minutes)
                return self.date
            except ValueError:
                print(''' __________________________''')
                print('''| Invalid date! try again. |''')
                print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')                
                continue