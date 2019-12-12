from Model.employee import Employee
from Model.voyage import Voyage
from Model.plane import Plane

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
        self.print_voyage_list(unmannedVoyages_list,voyageHeader_list)

    def print_voyage_list(self,voyage_list,header_list):

        print("{:<5}{:<10}{:<10}{:<15}{:<25}{:<25}{:<10}".format(
                header_list[0],header_list[1],header_list[2],header_list[3],header_list[4],header_list[5],header_list[6]))
        print(100 * "_")
        print()
        id_list = []
        for voyage in voyage_list:
            print("{:<5}{:<10}{:<10}{:<15}{:<25}{:<25}{:<10}".format(
                voyage[0],voyage[1],voyage[2],voyage[3],voyage[4],voyage[5],voyage[6]))
            id_list.append(int(voyage[0]))
        print()
        user_choice = input("Enter ID of voyage you want to staff: ")
        while int(user_choice) not in id_list:
            print("Invalid input!")
            print("Please enter an integer from {} to {}".format(min(id_list),max(id_list)))
            user_choice = input("Input: ")
        for voy in voyage_list:
            if voy[0] == user_choice:
                voyage = voy

        self.planeType = self.llAPI_in.getPlaneType(voyage[6])
        plane_obj = Plane(voyage[6], self.planeType)

        self.voyage_obj = Voyage(voyage[3],plane_obj,voyage[4],voyage[0])
        self.listAvailablePilots()
        self.listAvailableCabincrew()

    def listAvailablePilots(self):
        perfectPilots = self.llAPI_in.availablePilotsWithSpecificLicense(self.voyage_obj.departure,self.planeType)
        empID_list = []
        for pilot in perfectPilots:
            print("({}) {}".format(pilot['ID'],pilot['Name']))
            empID_list.append(pilot['ID'])

        user_choice = input("Enter ID of captain for voyage: ")
        valid_input = False
        while not valid_input:
            try:
                int(user_choice)
                valid_input = True
            except:
                print('Invalid input! Please enter a valid ID')
        while user_choice not in empID_list:
            print("ID incorrectly selected!")
            print("Try again!")
            user_choice = input("Enter ID of captain for voyage: ")
        empID_list.remove(user_choice)

        for pilot in perfectPilots:
            if pilot['ID'] == user_choice:
                captain = pilot['SSN']
                self.voyage_obj.assignCaptain(captain)
        
        user_choice = input("Enter ID of copilot for voyage: ")
        valid_input = False
        while not valid_input:
            try:
                int(user_choice)
                valid_input = True
            except:
                print('Invalid input! Please enter a valid ID')
        while user_choice not in empID_list:
            print("ID incorrectly selected!")
            print("Try again!")
            user_choice = input("Enter ID of copilot for voyage: ")

        for pilot in perfectPilots:
            if pilot['ID'] == user_choice:
                copilot = pilot['SSN']
                self.voyage_obj.assignCopilot(copilot)

    def listAvailableCabincrew(self):
        perfectFAs = self.llAPI_in.getAvailabiltyOfFAs(self.voyage_obj.departure, 'Available')
        empID_list = []
        for fa in perfectFAs:
            print('({}) {}'.format(fa['ID'], fa['Name']))
            empID_list.append(fa['ID'])
        
        user_choice = input("Enter ID of flight service manager for voyage: ")
        valid_input = False
        while not valid_input:
            try:
                int(user_choice)
                valid_input = True
            except:
                print('Invalid input! Please enter a valid ID')
        while user_choice not in empID_list:
            print("ID incorrectly selected!")
            print("Try again!")
            user_choice = input("Enter ID of flight service manager for voyage: ")
        empID_list.remove(user_choice)

        for fa in perfectFAs:
            if fa['ID'] == user_choice:
                fsm = fa['SSN']
                self.voyage_obj.assingFSM(fsm)

        user_choice = input("Enter ID of flight attendant for voyage: ")
        valid_input = False
        while not valid_input:
            try:
                int(user_choice)
                valid_input = True
            except:
                print('Invalid input! Please enter a valid ID')
        while user_choice not in empID_list:
            print("ID incorrectly selected!")
            print("Try again!")
            user_choice = input("Enter ID of flight attendant for voyage: ")
        empID_list.remove(user_choice)

        for fa in perfectFAs:
            if fa['ID'] == user_choice:
                fa1 = fa['SSN']
                self.voyage_obj.assignFA1(fa1)

        user_choice = input("Enter ID of flight attendant for voyage: ")
        valid_input = False
        while not valid_input:
            try:
                int(user_choice)
                valid_input = True
            except:
                print('Invalid input! Please enter a valid ID')
        while user_choice not in empID_list:
            print("ID incorrectly selected!")
            print("Try again!")
            user_choice = input("Enter ID of flight attendant for voyage: ")
        empID_list.remove(user_choice)

        for fa in perfectFAs:
            if fa['ID'] == user_choice:
                fa2 = fa['SSN']
                self.voyage_obj.assignFA2(fa2)
