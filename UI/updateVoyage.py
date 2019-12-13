from Model.voyage import Voyage
#from LL.LLAPI import LLAPI
from Model.plane import Plane
from Model.employee import Employee
import datetime

class UpdateVoyage():

    def __init__(self, llAPI_in):
        self.llAPI_in = llAPI_in

    def get_input(self):
        while True:
            print()
            print(''' ___________________________________________''')
            print('''|         NaN Air - Update Voyage           |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Update voyage                         |''')
            print('''| (2) Update contact information            |''')
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                list_of_voy = self.list_of_voyage()
                if list_of_voy == None:
                    return None
                elif list_of_voy == "back":
                    continue
            elif user_input == "2":
                if self.list_of_contact_list() == None:
                    return None
            elif user_input == "b":
                return "Back to voy_m"
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue


########### UPDATE CONTACT INFO ###############

    def list_of_contact_list(self):
        self.dest_list = self.llAPI_in.getDestinationsContactInfo()
        self.show_list(self.dest_list)

    def show_list(self, dest_list):
        counter = 0
        for line in dest_list:
            counter += 1
            dest = line[0]
            cont_name = line[1]
            cont_phone = line [2]
            print('({}) {:<25} {:<25} {:<7}'.format(counter,dest,cont_name,cont_phone))
    
        print () 
        self.id = int(input('What contact to update: '))
        self.id = self.id -1
        if self.display_info() == None:
            return None
        

    def display_info(self):
        self.cont_info_list = []

        self.dest = self.dest_list[self.id][0]
        self.contact_name = self.dest_list[self.id][1] 
        self.contact_phone = self.dest_list[self.id][2]
        while True:
            print()
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''| ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Destination: {:<29}| '''.format(self.dest))
            print('''|                                           |''')
            print('''|                                           |''')
            print('''|(1) Contact name: {:<25}| '''.format(self.contact_name))
            print('''|(2) Contact phone: {:<24}| '''.format(self.contact_phone))
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print() 
            user_input = input('Update: ')
            print()

            if user_input == "1":
                self.contact_name = input('Enter name: ')
                self.updated_info = self.contact_name
                self.row_index = 6
                
            elif user_input == "2":
                self.contact_phone = input('Enter phone number: ')
                self.updated_info = self.contact_phone
                self.row_index = 7
            
            else: 
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")  
                continue                  

            if self.confirm_contact_changes() == None:
                return None


    def confirm_contact_changes(self):
        while True:
            print()
            print(''' ___________________________________________''')
            print('''|   NaN Air - update contact information    |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Contact name: {:27} |'''.format(self.contact_name))
            print('''| Contact phone: {:26} |'''.format(self.contact_phone))
            print('''|                                           |''')
            print('''|                                           |''')
            print('''| Confirm changes?                          |''')
            print('''|                                           |''')
            print('''| (1) yes                                   |''')
            print('''| (2) no                                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                self.id = self.id + 1
                self.line_index = self.id
                self.llAPI_in.updateContactInfo(self.line_index, self.row_index, self.updated_info)
                if self.contact_confirmation() == None:
                    return None
            elif user_input == "2":
                return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")  
                continue                  


    def contact_confirmation(self):
        while True:
            print()
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Contact information successfullly updated!|''')
            print('''|                                           |''')
            print('''|                  __|__                    |''')
            print('''|              ---@-(")-@---                |''')
            print('''|                                           |''')
            print('''| (1) Update voyage                         |''')
            print('''| (2) Update contact information            |''')
            print('''|                                           |''')
            print('''| (3) Back to home page                     |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                if self.list_of_voyage() == None:
                    return None
            elif user_input == "2":
                if self.list_of_contact_list() == None:
                    return None
            elif user_input == "3":
                return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue



####### UPDATE VOYAGE ##########

    def list_of_voyage(self):
        id_list = []
        # Hérna prentast út listi af voyages
        # Fallið sér einnig um að villutjékka inputin hjá usernum - þeas að það sé in range
        # Og í lokin býr það til tilvik af voyage og planeType
        v_list,h_list = self.llAPI_in.getFullyStaffedVoyages()
        self.dict_of_voyages = self.llAPI_in.getVoyages()
        print()
        if v_list!= None and h_list != None:
            print("{:<5}{:<10}{:<10}{:<15}{:<25}{:<25}{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(
                h_list[0],h_list[1],h_list[2],h_list[3],h_list[4],
                h_list[5],h_list[6],h_list[7],h_list[8],h_list[9],h_list[10],h_list[11]))
            
            print("__"*90, "\n")

            for line in v_list:
                print("{:<5}{:<10}{:<10}{:<15}{:<25}{:<25}{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(
                line[0],line[1],line[2],line[3],line[4],
                line[5],line[6],line[7],line[8],line[9],line[10],line[11]))
                id_list.append(int(line[0]))
            print("\n\n")

            print()
            legal_input = False
            while legal_input == False:
                self.selectedVoyage = input("Enter ID of voyage to update: ")
                try:
                    int(self.selectedVoyage)
                    if int(self.selectedVoyage) not in id_list:
                        legal_input = False
                        print()
                        print("Error! The selected ID is not in range!")
                        print()
                        continue
                    else:
                        legal_input = True
                except ValueError:
                    print()
                    print("Error!")
                    print()
                    continue

        self.voy = []
        for line in v_list:
            if line[0] == self.selectedVoyage:
                self.voy.append(line)

        self.planeType = self.llAPI_in.getPlaneType(self.voy[0][6])
        self.plane_obj = Plane(self.voy[0][6], self.planeType) 
        self.dep_dt_obj = datetime.datetime.strptime(self.voy[0][4],"%Y-%m-%dT%H:%M:%S")
        self.dest_obj = self.llAPI_in.createDestinationObject(self.voy[0][3])

        self.voyage_obj = Voyage(self.dest_obj,self.plane_obj,self.dep_dt_obj,self.voy[0][0])
        self.voyage_obj.assignCaptain(self.voy[0][7])
        self.voyage_obj.assignCopilot(self.voy[0][8])
        self.voyage_obj.assingFSM(self.voy[0][9])
        self.voyage_obj.assignFA1(self.voy[0][10])
        self.voyage_obj.assignFA2(self.voy[0][11])

        self.date = str(self.voyage_obj.get_Departure().date())
        
        self.captain = self.voyage_obj.get_Captain()
        self.cop = self.voyage_obj.get_Copilot()
        self.fsm = self.voyage_obj.get_FSM()
        self.fa1 = self.voyage_obj.get_FA1()
        self.fa2 = self.voyage_obj.get_FA2()

        choose_emp = self.choose_employees()
        if choose_emp == "back":
            return "back"
        elif choose_emp == None:
            return None

    def choose_employees(self):
        while True:
            print()
            print(''' ___________________________________________''')
            print('''|         NaN Air - Update Voyage           |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Update pilots                         |''')
            print('''| (2) Update cabincrew                      |''')
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                if self.get_pilots_on_voyage() == None:
                    return None
            elif user_input == "2":
                if self.get_fas_on_voyage() == None:
                    return None
            elif user_input == "b":
                return "back"
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue
            self.replace_employee()
    
    def replace_employee(self):
        if self.update_FA == True:          # Ef við förum in í listofAvailableFA þá er þetta satt 
                                            # Og gefur nýja starfsmanninum rétt gildi eftir því sem á við

            if self.user_input == "1":
                self.fsm = self.new_emp_ssn

            elif self.user_input == "2":
                self.fa1 = self.new_emp_ssn

            elif self.user_input == "3":
                self.fa2 = self.new_emp_ssn

        else:
            if self.user_input == "1":
               self.captain = self.new_emp_ssn
            
            elif self.user_input == "2":
                self.cop = self.new_emp_ssn

        if self.find_new_employee() == None:
            return None
    
    def find_new_employee(self):
        if self.confirm_voyage_changes()  == None:
            return None
    
    def confirm_voyage_changes(self):
        destination = self.voyage_obj.get_destination()
        print() 
        print()
        print(''' ___________________________________________''')
        print('''|         NaN Air -  Confirm Changes        |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print('''Captain:                   {}                                        '''.format(self.captain))
        print('''Copilot:                   {}                                        '''.format(self.cop))
        print('''Flight service Manager:    {}                                        '''.format(self.fsm))
        print('''Flight attendant 1:        {}                                        '''.format(self.fa1))
        print('''Flight attendant 2:        {}                                        '''.format(self.fa2))
        print('''Departure time:            {}                                        '''.format(self.voyage_obj.get_Departure()))
        print('''Destination:               {}                                        '''.format(destination.get_destination()))
        print()

        print('''(1) Yes''')
        print('''(2) No''')
        print()
        user_input = input("Input: ")
        legal_input = False
        while legal_input == False:
            
            if user_input == "1":
                if self.update_employee_of_voyage() == None:
                    return None
                legal_input = True

            elif user_input == "2":
                legal_input = True
                return None
        
            else: 
                print("Error! Please enter 1 or 2!")
                user_input = input("Input: ")
    
    def voyage_confirmation(self):
        while True:
            print()
            print()
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Voyage successfullly updated!             |''')
            print('''|                                           |''')
            print('''|                   __|__                   |''')
            print('''|               ---@-(")-@---               |''')
            print('''|                                           |''')
            print('''| (1) Update voyage                         |''')
            print('''| (2) Update contact information            |''')
            print('''|                                           |''')
            print('''| (3) Back to home page                     |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                if self.list_of_voyage() == None:
                    return None
            elif user_input == "2":
                if self.list_of_contact_list() == None:
                    return None
            elif user_input == "3":
                return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue


    def get_fas_on_voyage(self):
        self.update_FA = True
        self.update_Pilot = False
        while True:
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''|          Select FA to update:             |''')
            print('''|                                           |''')
            print('''| (1)      {:33}|'''.format(self.fsm))
            print('''| (2)      {:33}|'''.format(self.fa1))
            print('''| (3)      {:33}|'''.format(self.fa2))
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
            print()
            self.user_input = input("Input: ") 
            print()
            if self.user_input == '1' or self.user_input == '2' or self.user_input == '3':
                if self.available_fa() == None:
                    return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue


    def get_pilots_on_voyage(self):
        self.update_Pilot = True
        self.update_FA = False
        while True:
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''|         Select Pilot to update:           |''')
            print('''|                                           |''')           
            print('''| (1)      {:33}|'''.format(self.captain))
            print('''| (2)      {:33}|'''.format(self.cop))
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
            print()
            self.user_input = input("Input: ")
            print()
            if self.user_input == '1' or self.user_input == '2':
                if self.available_pilots() == None:
                    return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue


    def available_fa(self):
        dict_of_avaliable = self.llAPI_in.getAvailabiltyOfFAs(self.date,"Available")
        h_list = self.llAPI_in.getEmployeeHeader(dict_of_avaliable)
        v_list = self.llAPI_in.getEmployeeValue(dict_of_avaliable)
        id_list = []
        for line in v_list:
            id_list.append(line[0])

        print()

        print("Select new FA for voyage")

        print()

        print("{:<10}{:<20}{:<30}{:<20}".format(h_list[0],h_list[1],h_list[2],h_list[4]))
        print("__"*42)

        for line in v_list:
            print("{:<10}{:<20}{:<30}{:<20}".format(line[0],line[1],line[2],line[4]))
        
        print()
        user_input = input("Enter ID of employee: ")

        print()
        legal_input = False
        while legal_input == False:
            if user_input not in id_list:
                print("Error please select a valid ID")
                user_input = input("Enter ID of employee: ")

            else:
                legal_input = True
        
        index_of_new_emp = id_list.index(user_input)
        self.new_emp_ssn = v_list[index_of_new_emp][1]

        self.replace_employee()
    
    
    def available_pilots(self):
        dict_of_avaliable = self.llAPI_in.availablePilotsWithSpecificLicense(self.date,self.planeType)
        h_list = self.llAPI_in.getEmployeeHeader(dict_of_avaliable)
        v_list = self.llAPI_in.getEmployeeValue(dict_of_avaliable)
        id_list = []
        for line in v_list:
            id_list.append(line[0])

        print()

        print("Select new Pilot for voyage")

        print()

        print("{:<10}{:<20}{:<30}{:<20}".format(h_list[0],h_list[1],h_list[2],h_list[4]))
        print("__"*42)

        for line in v_list:
            print("{:<10}{:<20}{:<30}{:<20}".format(line[0],line[1],line[2],line[4]))
        
        print()
        user_input = input("Enter ID of employee: ")

        print()
        legal_input = False
        while legal_input == False:
            if user_input not in id_list:
                print("Error please select a valid ID")
                user_input = input("Enter ID of employee: ")
            else:
                legal_input = True
        
        index_of_new_emp = id_list.index(user_input)
        self.new_emp_ssn = v_list[index_of_new_emp][1]
        #print(self.new_emp_ssn)

        if self.replace_employee() == None:
            return None


    def update_employee_of_voyage(self):
        if self.update_Pilot == True:
            if self.user_input == "1":
                self.voyage_obj.assignCaptain(self.new_emp_ssn)
                
            elif self.user_input == "2":
                self.voyage_obj.assignCopilot(self.new_emp_ssn)
            else: 
                print("balalsd")

        else:
            if self.user_input == "1":
                self.voyage_obj.assingFSM(self.new_emp_ssn)
            
            if self.user_input == "2":
                self.voyage_obj.assignFA1(self.new_emp_ssn)

            elif self.user_input == "3":
                self.voyage_obj.assignFA2(self.new_emp_ssn)

        self.llAPI_in.storeCrewToFile(self.voyage_obj)
        if self.voyage_confirmation() == None:
            return None



