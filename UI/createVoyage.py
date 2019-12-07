from Model.voyage import Voyage


class CreateVoyage():
    def get_input(self):
        while True:
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
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
        print("Destinations")
        print("Vantar lista fra data")
    
    def enter_destination_details(self):
        self.date = input("Enter date of departure: ")
        self.time = input("Enter time of departure: ")
        self.flight_number = input("Enter flight number: ")

    def review_voyage_info(self):
        while True:
            print(''' ___________________________________________''')
            print('''|       NaN Air - Review information        |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Flight number: {:27}|'''.format(self.flight_number))
            print('''| Date of departure: {:23}|'''.format(self.date))
            print('''| Time of departure: {:23}|'''.format(self.role))
            print('''| Date of trip back: {:23}|'''.format(self.address))
            print('''| Time of trip back: {:23}|'''.format(self.phone_no))
            print('''|                                           |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Confirm                               |''')
            print('''| (2) Edit                                  |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")            

    def edit_voyage_info(self):
        while True:
            print(''' ___________________________________________''')
            print('''|       NaN Air - Edit information          |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Flight number: {:23}|'''.format(self.flight_number))
            print('''| (2) Date of departure: {:19}|'''.format(self.date))
            print('''| (3) Time of departure: {:19}|'''.format(self.role))
            print('''| (4) Date of trip back: {:19}|'''.format(self.address))
            print('''| (5) Time of trip back: {:19}|'''.format(self.phone_no))
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ") 
            if user_input == "1":
                self.flight_number = input("Enter flight number: ")
                if self.review_voyage_info() == None:
                    return None
            elif user_input == "2":
                self.name = input("Enter date of departure: ")
                if self.review_voyage_info() == None:
                    return None
            elif user_input == "3":
                self.role = self.get_role()
                if self.display_info() == None:
                    return None
            elif user_input == "4":
                self.rank = input("Enter rank: ")
                if self.display_info() == None:
                    return None
            elif user_input == "5":
                self.address = input("Enter address: ")
                if self.display_info() == None:


########### create new destination #######################################

    def get_destination_info(self):
        #print()
        print(' _________________________________________')
        print("| NaN Air - Enter destination information |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
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
            #print()
            user_input = input("Input: ")
            if user_input == '1':
                if self.print_confirmation_destination() == None:
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
            print('''| (1) Country: {:29}|'''.format(self.country))
            print('''| (2) Airport: {:29}|'''.format(self.airport))
            print('''| (3) Airline: {:29}|'''.format(self.airline))
            print('''| (4) Distance: {:28}|'''.format(self.distance))
            print('''| (5) Contact name: {:24}|'''.format(self.contact_name))
            print('''| (6) Contact phone: {:23}|'''.format(self.contact_phone))
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Edit selection: ")
            if user_input == '1':
                self.country = input("Enter country: ")
                if self.display_destination_info() == None:
                    return None
            elif user_input == '2':
                self.airport = input("Enter airport: ")
                if self.display_destination_info() == None:
                    return None
            elif user_input == '3':
                self.airline = input("Enter airline: ")
                if self.display_destination_info() == None:
                    return None
            elif user_input == '4':
                self.distance = input("Enter distance: ")
                if self.display_destination_info() == None:
                    return None
            elif user_input == '5':
                self.contact_name = input("Enter contact name: ")
                if self.display_destination_info() == None:
                    return None
            elif user_input == '6':
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
        self.voyage = Voyage(self.country, self.airport, self.airline, self.distance, self.contact_name, self.contact_phone)
        self.print_confirmation_destination()
        return self.voyage
