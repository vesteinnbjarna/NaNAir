from Model.voyage import Voyage
from Model.Destination import Destination


class CreateVoyage():
    def __init__(self, llAPI_in):
        self.llAPI_in = llAPI_in
        
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
            if user_input == "1":
                self.select_destination()
            elif user_input == "2":
                pass
            elif user_input == "3":
                if self.get_destination_info() == None:
                    return None
            elif user_input == "b":
                return "Back to voy_m"
            else:
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
            #line_index = 0
            for line in destination_list:
                for key, val in line.items():
                    if key == "destination":
                        print("({}) {}".format(counter,val))
                        counter += 1
                        dest_list.append(val)
               # line_index += 1
            print('''                                             ''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            print()
            try:
                if int(user_input) in range(len(dest_list) + 1):
                    self.chosen_destinaiton = dest_list[int(user_input) - 1]
                    self.enter_destination_details()
            except:
                ValueError
                continue

   # def get_aircraft_list(self):
   #     available_aircraft_list = self.

    def enter_destination_details(self):
        print()
        self.date = input("Enter date of departure (yyyy-mm-dd): ")
        self.time_depart = input("Enter time of departure (hh:mm): ")
        #self.aircraft = 
        #self.time_back = input("Enter time of trip back (hh:mm): ")
        #self.flight_number = input("Enter flight number: ")
        self.review_voyage_info()

    def review_voyage_info(self):
        while True:
            print(''' ___________________________________________''')
            print('''|       NaN Air - Review information        |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Chosen destination: {:22}|'''.format(self.chosen_destinaiton))
          #  print('''| Flight number: {:27}|'''.format(self.flight_number))
            print('''| Date of departure: {:23}|'''.format(self.date))
            print('''| Time of departure: {:23}|'''.format(self.time_depart+":00"))
            print('''| Date of trip back: {:23}|'''.format(self.date))
          #  print('''| Time of trip back: {:23}|'''.format(self.time_back +":00"))
            print('''|                                           |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Confirm                               |''')
            print('''| (2) Edit                                  |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")  
            if user_input == "1":
                self.




    # def edit_voyage_info(self):
    #     while True:
    #         print(''' ___________________________________________''')
    #         print('''|       NaN Air - Edit information          |''')
    #         print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
    #         print('''| (1) Flight number: {:23}|'''.format(self.flight_number))
    #         print('''| (2) Date of departure: {:19}|'''.format(self.date))
    #         print('''| (3) Time of departure: {:19}|'''.format("test"))
    #         print('''| (4) Date of trip back: {:19}|'''.format("test"))
    #         print('''| (5) Time of trip back: {:19}|'''.format("test"))
    #         print('''|                                           |''')
    #         print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
    #         user_input = input("Input: ") 
    #         if user_input == "1":
    #             self.flight_number = input("Enter flight number: ")
    #             if self.review_voyage_info() == None:
    #                 return None
    #         elif user_input == "2":
    #             self.name = input("Enter date of departure: ")
    #             if self.review_voyage_info() == None:
    #                 return None
    #         elif user_input == "3":
    #             self.role = self.get_role()
    #             if self.display_info() == None:
    #                 return None
    #         elif user_input == "4":
    #             self.rank = input("Enter rank: ")
    #             if self.display_info() == None:
    #                 return None
    #         elif user_input == "5":
    #             self.address = input("Enter address: ")
    #             if self.display_info() == None:
    #                 return None


########### create new destination #######################################

    def get_destination_info(self):
        #print()
        print(' _________________________________________')
        print("| NaN Air - Enter destination information |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
        self.destination = input("Enter destination: ")
        self.country = input(" Enter country: ")
        self.airport = input(" Enter airport: ")
        self.airline = input(" Enter airline: ")
        self.distance = input(" Enter distance: ")
        self.contact_name = input(" Enter contact name: ")  
        self.contact_phone = input(" Enter contact phone: ")
        self.display_destination_info()

    def display_destination_info(self):
        while True:
            print(''' ___________________________________________''')
            print('''| NaN Air - Review destination information  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Destination: {:26}|'''.format(self.destination))
            print('''| Country: {:33}|'''.format(self.country))
            print('''| Airport: {:33}|'''.format(self.airport))
            print('''| Airline: {:33}|'''.format(self.airline))
            print('''| Distance: {:32}|'''.format(self.distance))
            print('''| Contact name: {:28}|'''.format(self.contact_name))
            print('''| Contact phone: {:27}|'''.format(self.contact_phone))
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
                continue

    def edit_info(self):
        while True:
            print(''' ___________________________________________''')
            print('''|  NaN Air - Edit destination information   |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Destination: {:25}|'''.format(self.destination))
            print('''| (2) Country: {:29}|'''.format(self.country))
            print('''| (3) Airport: {:29}|'''.format(self.airport))
            print('''| (4) Airline: {:29}|'''.format(self.airline))
            print('''| (5) Distance: {:28}|'''.format(self.distance))
            print('''| (6) Contact name: {:24}|'''.format(self.contact_name))
            print('''| (7) Contact phone: {:23}|'''.format(self.contact_phone))
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
                self.airline = input("Enter airline: ")
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
                continue
            

    def print_confirmation_destination(self):
        while True:
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Destination successfully created!         |''')
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
                continue


    def create_destination(self):
        self.dest = Destination(self.destination, self.country, self.airport, self.airline, self.distance, self.contact_name, self.contact_phone)
        #self.print_confirmation_destination()
        self.llAPI_in.createDestination(self.dest)
        return self.dest

    # def create_voyage(self):
    #     self.voy = Voyage(self.flight_number, )

#flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftID