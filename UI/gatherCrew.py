from Model.employee import Employee
from Model.voyage import Voyage
from Model.plane import Plane
import datetime

# Get list of unmanned voyages
# Choose voyage to man
# Get list of availabla pilots with correct license
# Choose captain and coplot
# Get list of available flight attendants
# Choose flight service manager and two flight attendants

class GatherCrew():
    def __init__(self, llAPI_in):
        self.llAPI_in = llAPI_in


    def getListOfUnmannedVoyages(self):
        unmannedVoyages_list, voyageHeader_list = self.llAPI_in.getUnmannedVoyages()
        if self.print_voyage_list(unmannedVoyages_list,voyageHeader_list) == None:
            return None


    def print_voyage_list(self,voyage_list,header_list):
        if header_list == None:
            print(''' ___________________________________________''')
            print('''|      All voyages are fully staffed!       |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
            print()
            input("Press enter to go back to home page!")
            print()
            
        else:
            print("{:<5}{:<10}{:<10}{:<15}{:<25}{:<25}{:<10}".format(
                    header_list[0],header_list[1],header_list[2],header_list[3],header_list[4],header_list[5],header_list[6]))
            print(100 * "_")
            print()
            id_list = []
            for voyage in voyage_list:
                print("{:<5}{:<10}{:<10}{:<15}{:<25}{:<25}{:<10}".format(
                    voyage[0],voyage[1],voyage[2],voyage[3],voyage[4],voyage[5],voyage[6]))
                id_list.append(int(voyage[0]))
            
            while True:
                print()
                user_choice = input("Enter ID of voyage you want to staff: ")
                print()
                try:
                    user_choice = int(user_choice)
                except:
                    print()
                    print("Invalid input!")
                    print("Please enter valid ID")
                    continue

                if int(user_choice) not in id_list:
                    print("Invalid input!")
                    print("Please enter valid ID")
                    continue

                for voy in voyage_list:
                    if voy[0] == user_choice:
                        voyage = voy
                break      


            self.planeType = self.llAPI_in.getPlaneType(voyage[6])
            plane_obj = Plane(voyage[6], self.planeType)

            destination_obj = self.createDestinationObject(voyage[3])
            departure_datetime = datetime.datetime.strptime(voyage[4], '%Y-%m-%dT%H:%M:%S')


            self.voyage_obj = Voyage(destination_obj,plane_obj,departure_datetime,voyage[0])
            self.listAvailablePilots()
            self.listAvailableCabincrew()
            if self.print_crew_review() == None:
                return None
                
            # Mögulega henda edit möguleika hérna  

    def createDestinationObject(self,destination_str):
        destination_obj = self.llAPI_in.createDestinationObject(destination_str)
        return destination_obj

    def listAvailablePilots(self):
        '''Method that asks user to choose a captain and copilot for voyage.'''
        perfectPilots = self.llAPI_in.availablePilotsWithSpecificLicense(self.voyage_obj.departure,self.planeType)
        empID_list = []
        print()
        print(''' ___________________________________________''')
        print('''|         Select pilots for voyage          |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
        print()
        for pilot in perfectPilots:
            print(" ({}) {}".format(pilot['ID'],pilot['Name']))
            empID_list.append(pilot['ID'])

        # User chooses captain with the employee ID.
        print()
        user_choice = input("Enter ID of captain for voyage: ")
        valid_input = False
        while not valid_input:
            try:
                int(user_choice)
                valid_input = True
            except:
                print()
                print('Invalid input! Please enter a valid ID')
        while user_choice not in empID_list:
            print()
            print("ID incorrectly selected!")
            print("Try again!")
            print()
            user_choice = input("Enter ID of captain for voyage: ")
        empID_list.remove(user_choice)

        #Assign captain to crew for voyage.
        for pilot in perfectPilots:
            if pilot['ID'] == user_choice:
                captain = pilot['SSN']
                self.captain_name = pilot['Name']
                self.voyage_obj.assignCaptain(captain)
        
        #User chooses copilot for voyage with employee ID.
        print()
        user_choice = input("Enter ID of copilot for voyage: ")
        valid_input = False
        while not valid_input:
            try:
                int(user_choice)
                valid_input = True
            except:
                print('Invalid input! Please enter a valid ID')
        while user_choice not in empID_list:
            print()
            print("ID incorrectly selected!")
            print("Try again!")
            print()
            user_choice = input("Enter ID of copilot for voyage: ")

        for pilot in perfectPilots:
            if pilot['ID'] == user_choice:
                copilot = pilot['SSN']
                self.copilot_name = pilot['Name']
                self.voyage_obj.assignCopilot(copilot)
        print()
        print(''' ___________________________________________''')
        print('''|   Pilots have been assigned to Voyage!    |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''|                                           |''')
        print('''| CAPTAIN: {:33}|'''.format(self.captain_name))
        print('''|                                           |''')
        print('''| COPILOT: {:33}|'''.format(self.copilot_name))
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
        print()
        input('Press enter to choose FAs for Voyage!')

    def listAvailableCabincrew(self):
        ''' Method that asks user to choose FSM, FA1 and FA2 for voyage. '''
        perfectFAs = self.llAPI_in.getAvailabiltyOfFAs(self.voyage_obj.departure, 'Available')
        empID_list = []
        print()
        print(''' ___________________________________________''')
        print('''|    Select flight attendans for voyage     |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
        print()
        for fa in perfectFAs:
            print(' ({}) {}'.format(fa['ID'], fa['Name']))
            empID_list.append(fa['ID'])
        print()
        user_choice = input("Enter ID of flight service manager for voyage: ")
        valid_input = False
        while not valid_input:
            try:
                int(user_choice)
                valid_input = True
            except:
                print()
                print('Invalid input! Please enter a valid ID')
        while user_choice not in empID_list:
            print()
            print("ID incorrectly selected!")
            print("Try again!")
            print()
            user_choice = input("Enter ID of flight service manager for voyage: ")
            print()
        empID_list.remove(user_choice)

        for self.fa in perfectFAs:
            if self.fa['ID'] == user_choice:
                self.fsm = self.fa['SSN']
                self.fsm_name = self.fa['Name']
                self.voyage_obj.assingFSM(self.fsm)

        print()
        user_choice = input("Enter ID of flight attendant for voyage: ")
        valid_input = False
        while not valid_input:
            try:
                int(user_choice)
                valid_input = True
            except:
                print()
                print('Invalid input! Please enter a valid ID')
        while user_choice not in empID_list:
            print()
            print("ID incorrectly selected!")
            print("Try again!")
            print()
            user_choice = input("Enter ID of flight attendant for voyage: ")
            print()
        empID_list.remove(user_choice)

        for self.fa in perfectFAs:
            if self.fa['ID'] == user_choice:
                self.fa1 = fa['SSN']
                self.fa1_name = fa['Name']
                self.voyage_obj.assignFA1(self.fa1)

        print()
        user_choice = input("Enter ID of flight attendant for voyage: ")
        print()
        valid_input = False
        while not valid_input:
            try:
                int(user_choice)
                valid_input = True
            except:
                print('Invalid input! Please enter a valid ID')
        while user_choice not in empID_list:
            print()
            print("ID incorrectly selected!")
            print("Try again!")
            print()
            user_choice = input("Enter ID of flight attendant for voyage: ")
            print()
        empID_list.remove(user_choice)

        for fa in perfectFAs:
            if fa['ID'] == user_choice:
                self.fa2 = fa['SSN']
                self.fa2_name = fa['Name']
                self.voyage_obj.assignFA2(self.fa2)
        

        
        
    def print_crew_review(self):
        ''' Method that prints out a review of the new crew and asks user to confirm the crew or cancel.'''
        while True:    
            print()
            print(''' ___________________________________________''')
            print('''|   New Crew has been assigned to Voyage!   |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''|                                           |''')
            print('''| CAPTAIN: {:33}|'''.format(self.captain_name))
            print('''|                                           |''')
            print('''| COPILOT: {:33}|'''.format(self.copilot_name))
            print('''|                                           |''')
            print('''| FSM: {:37}|'''.format(self.fsm_name))
            print('''|                                           |''')
            print('''| FA1: {:37}|'''.format(self.fa1_name))
            print('''|                                           |''')   
            print('''| FA2: {:37}|'''.format(self.fa2_name))
            print('''|                                           |''')    
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Confirm voyage                        |''')  
            print('''| (2) Cancel voyage                         |''')
            print('''|                                           |''')     
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
            user_input = input("Input: ")
            print()
            if user_input == "1":
                self.storeCrewToFile(self.voyage_obj)
                if self.crewSuccessfullyAddedToVoyage() == None:
                    return None
            elif user_input == "2":
                return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    


        
    def storeCrewToFile(self,voyage):
        self.llAPI_in.storeCrewToFile(voyage)


    def crewSuccessfullyAddedToVoyage(self):
        print()
    
        print(''' ___________________________________________''')
        print('''|       Voyage successfully staffed!        |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''|                                           |''')
        print('''|                  __|__                    |''')
        print('''|              ---@-(")-@---                |''')
        print('''|                                           |''')
        print('''|    Press enter go to back to homepage!    |''')
        print('''|                                           |''')  
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
        user_input = input()
        return None