from Model.voyage import Voyage
from Model.Destination import Destination
from Model.plane import Plane
from UI.gatherCrew import GatherCrew
import datetime

class CreateVoyage():
    def __init__(self, llAPI_in):
        self.llAPI_in = llAPI_in
        self.gaterCrew = GatherCrew(llAPI_in)
        
    def get_input(self):
        self.departingFrom = "REY"
        while True:
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Create new voyage                     |''')
            print('''| (2) Gather crew for voyage                |''')
            print('''| (3) Create destination                    |''')
            print('''|                                           |''')
            print('''| press 'b' for back                        |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')       
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                if self.select_destination() == "Back to home":
                    return None
            elif user_input == "2":
                if self.gaterCrew.getListOfUnmannedVoyages() == None:
                    return None 
            elif user_input == "3":
                if self.get_destination_info() == None:
                    return None
            elif user_input == "b":
                return "Back to voy_m"
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")    
                continue

########### create new voyage #######################################

    def select_destination(self):
        while True:
            destination_list = self.llAPI_in.getDestinations()
            self.chosen_destinaiton = ""
            dest_list = []
            print(''' ___________________________________________''')
            print('''|     NaN Air - List of destinations        |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
            counter = 1
            for line in destination_list:
                for key, val in line.items():
                    if key == "Destination":
                        print("({}) {}".format(counter,val))
                        counter += 1
                        dest_list.append(val)
            print('''                                             ''')
            print('''   press "b" to go back                      ''')
            print('''                                             ''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            print()

            if user_input == "b":
                return None

            valid_input = False
            while valid_input == False:
                try:
                    int(user_input)
                    dest_list[int(user_input) - 1]
                    valid_input = True
                except:
                    print('Invalid input! Please enter an integer from 1 to {}'.format(len(dest_list)))
                    user_input = input("Input: ")

            for destination in destination_list:
                if destination['Destination'] == dest_list[int(user_input) - 1]:
                    destination_line = destination
            self.chosen_destinaiton = Destination(destination_line['Destination'],destination_line['Country'],\
                destination_line['Airport'],destination_line['Airtime'],destination_line['Distance'],\
                    destination_line['Contact name'],destination_line['Contact phone'])
            if self.enter_voyage_details() == "Back to home":
                return "Back to home"

    def get_availalbe_aircraft_list(self):
        totalTime = self.chosen_destinaiton.totalTime
        available_aircrafts_list = self.llAPI_in.getAvailablePlanes(self.dateTime, totalTime)
        print(''' ___________________________________________''')
        print('''|         NaN Air - Choose aircraft         |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        counter = 1
        line_list = []
        working_list = []
        for aircraft in available_aircrafts_list:
            print(' ({})'.format(counter), end=" ")
            for val in aircraft.values():
                print(val, end="  ")
                line_list.append(val)
            working_list.append(line_list)
            line_list = []
            print()
            counter += 1
        print()
        user_choice = input("Input: ")
        chosen_aircraft_registration = working_list[int(user_choice) - 1][0]
        chosen_aircraft_type = working_list[int(user_choice) - 1][1]
        self.chosen_aircraft = Plane(chosen_aircraft_registration, chosen_aircraft_type)
        return None

    def enter_voyage_details(self): 
        print()
        #self.date = input("Enter date of departure (yyyy-mm-dd): ")
        #self.time_depart = input("Enter time of departure (hh:mm): ")

        valid_input = False
        while valid_input == False:
            year_str = input("Enter year: ")
            month_str = input("Enter month: ")
            day_str = input("Enter day: ")
            year_int = self.check_input(year_str)
            month_int = self.check_input(month_str)
            day_int = self.check_input(day_str)
            self.time = input("Enter departure time (hh:mm): ")
            try:
                hours_int = int(self.time[:2])
                minutes_int = int(self.time[3:])
            except ValueError:
                print()
                print(" Invalid airtime, must be integer!")
                print()
                continue 
            self.dateTime = datetime.datetime(year_int,month_int,day_int,hours_int,minutes_int)
            if not self.llAPI_in.checkDateTime(self.dateTime):
                print()
                print('Another voyage is departing at this time!')
                print('Please select another time :-)')
                print()
                continue
            else:
                valid_input = True

        self.get_availalbe_aircraft_list()
        if self.create_voyage_object() == "Back to home":
            return "Back to home"

    def check_input(self, a_str):
        invalid_input = True
        while invalid_input == True:
            try:
                a_int = int(a_str)
                return a_int
            except ValueError:
                print()
                print("Invalid input! Must be integer. ")
                print()
                continue


    def review_voyage_info(self):
        while True:
            print(''' ___________________________________________''')
            print('''|       NaN Air - Review information        |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Chosen destination: {:<22}|'''.format(self.chosen_destinaiton.destination))
            print('''| Date of departure: {:<23}|'''.format(str(self.dateTime.date())))
            print('''| Time of departure: {:<23}|'''.format(str(self.dateTime.time())))
            print('''| Date of arrival: {:<25}|'''.format(str((self.voyage.get_Departure() + self.chosen_destinaiton.totalTime).date())))
            print('''| Time of arrival: {:<25}|'''.format(str((self.voyage.get_Departure() + self.chosen_destinaiton.totalTime).time())))
            print('''| Aircraft registration: {:<19}|'''.format(self.chosen_aircraft.registration))
            print('''|                                           |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Confirm                               |''')
            print('''| (2) Cancel                                |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            print()
            if user_input == "1":
                self.llAPI_in.createVoyage(self.voyage)
                if self.print_confirmation_voyage() == "Back to home":
                    return "Back to home"
                return None
            elif user_input == "2":
                return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue

    def create_voyage_object(self):
        self.voyage = Voyage(self.chosen_destinaiton, self.chosen_aircraft,self.dateTime)
        if self.review_voyage_info() == "Back to home":
            return "Back to home"

    def print_confirmation_voyage(self):
        while True:
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Voyage successfully created!              |''')
            print('''|                                           |''')
            print('''|                  __|__                    |''')
            print('''|              ---@-(")-@---                |''')
            print('''|                                           |''')
            print('''| (1) Create another voyage                 |''')
            print('''| (2) Go back to home page                  |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ") 
            if user_input == "1":
                return None
            elif user_input == "2":
                return "Back to home"
            else:
                continue
            

########### create new destination #######################################

    def get_destination_info(self):
        ''' Method that gets information about new destination from user. '''
        print(' _________________________________________')
        print("| NaN Air - Enter destination information |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
        self.destination = input(" Enter destination: ")
        self.country = input(" Enter country: ")
        self.airport = input(" Enter airport: ")
        invalid_input = True
        while invalid_input == True:
            self.airtime = input(" Enter airtime (hh:mm): ")
            try:
                int(self.airtime[:2])
                int(self.airtime[3:])
                invalid_input = False
            except ValueError:
                print()
                print(" Invalid airtime, must be integer!")
                print()
                continue
        self.distance = input(" Enter distance: ")
        self.contact_name = input(" Enter contact name: ")  
        self.contact_phone = input(" Enter contact phone: ")
        self.display_destination_info()

    def display_destination_info(self):
        ''' Method that displays '''
        while True:
            print(''' ___________________________________________''')
            print('''| NaN Air - Review destination information  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Destination: {:<29}|'''.format(self.destination))
            print('''| Country: {:<33}|'''.format(self.country))
            print('''| Airport: {:<33}|'''.format(self.airport))
            print('''| Airtime: {:<33}|'''.format(self.airtime))
            print('''| Distance: {:<32}|'''.format(self.distance))
            print('''| Contact name: {:<28}|'''.format(self.contact_name))
            print('''| Contact phone: {:<27}|'''.format(self.contact_phone))
            print('''|                                           |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Confirm                               |''')
            print('''| (2) Edit                                  |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            if user_input == '1':
                if self.create_destination():
                    self.print_confirmation_destination()
                    return None
            elif user_input == '2':
                if self.edit_info() == None:
                    return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue

    def edit_info(self):
        while True:
            print(''' ___________________________________________''')
            print('''|  NaN Air - Edit destination information   |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Destination: {:<25}|'''.format(self.destination))
            print('''| (2) Country: {:<29}|'''.format(self.country))
            print('''| (3) Airport: {:<29}|'''.format(self.airport))
            print('''| (4) Airtime: {:<29}|'''.format(self.airtime))
            print('''| (5) Distance: {:<28}|'''.format(self.distance))
            print('''| (6) Contact name: {:<24}|'''.format(self.contact_name))
            print('''| (7) Contact phone: {:<23}|'''.format(self.contact_phone))
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Edit selection: ")
            if user_input == '1':
                self.destination = input("Enter destination: ")
                if self.display_destination_info() == None:
                    return None
            elif user_input == '2':
                self.country = input("Enter country: ")
                if self.display_destination_info() == None:
                    return None
            elif user_input == '3':
                self.airport = input("Enter airport: ")
                if self.display_destination_info() == None:
                    return None
            elif user_input == '4':
                self.airtime = input("Enter airtime: ")
                if self.display_destination_info() == None:
                    return None
            elif user_input == '5':
                self.distance = input("Enter distance: ")
                if self.display_destination_info() == None:
                    return None
            elif user_input == '6':
                self.contact_name = input("Enter contact name: ")
                if self.display_destination_info() == None:
                    return None
            elif user_input == '7':
                self.contact_phone = input("Enter contact phone: ")
                if self.display_destination_info() == None:
                    return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue
            

    def print_confirmation_destination(self):
        while True:
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Destination successfully created!         |''')
            print('''|                                           |''')
            print('''|                  __|__                    |''')
            print('''|              ---@-(")-@---                |''')
            print('''|                                           |''')
            print('''| (1) Create another destination            |''')
            print('''| (2) Go back to home page                  |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            if user_input == "1":
                if self.get_destination_info() == None:
                    return None
            elif user_input == "2":
                return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue


    def create_destination(self):
        self.dest = Destination(self.destination, self.country, self.airport, self.airtime, self.distance, self.contact_name, self.contact_phone)
        self.llAPI_in.createDestination(self.dest)
        return self.dest

