from Model.voyage import Voyage
#from LL.LLAPI import LLAPI

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
                if self.list_of_voyage() == None:
                    return None
            elif user_input == "2":
                if self.list_of_contact_list() == None:
                    return None
            elif user_input == "b":
                return "Back to voy_m"
            else:
                continue


########### UPDATE CONTACT INFO ###############

    def list_of_contact_list(self):
        #Senda uppl á data layer um að fá lista af contacts
        #print("#####Prentast út listi frá data layer####") #####
        self.dest_list = self.llAPI_in.getDestinationsContactInfo()
        self.show_list(self.dest_list)
        # display_info()
        # self.update_contact_info()

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
        self.display_info()
        

    def display_info(self):
        self.cont_info_list = []

        self.dest = self.dest_list[self.id][0]
        self.contact_name = self.dest_list[self.id][1] 
        self.contact_phone = self.dest_list[self.id][2]

        print()
        print(''' ___________________________________________''')
        print('''|                  NaN Air                  |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print('''    Destination: {} '''.format(self.dest))
        print('''(1) Contact name: {} '''.format(self.contact_name))
        print('''(2) Contact phone {} '''.format(self.contact_phone))
        #print('''(3) Update both                             ''')
        print('''                                            ''')
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
        
        # elif user_input == "3":
        #     self.cont_name = input('Enter name: ')
        #     self.updated_info = self.cont_name
        #     self.cont_phone = input('Enter phone number: ')
        #     self.updated_info = self.cont_phone
        
        else:
            print('u suck')
            
        self.confirm_contact_changes()


    # def update_contact_info(self):
    #      # Velur hvort hann vilji update contact name, number eða bæði
    #     self.contact_name = ""
    #     self.contact_phone = ""
    #     print()
    #     print(''' ___________________________________________''')
    #     print('''|   NaN Air - update contact information    |''')
    #     print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
    #     print('''| (1) Contact name                          |''')
    #     print('''| (2) Contact phone number                  |''')
    #     print('''| (3) both                                  |''')
    #     print('''|                                           |''')
    #     print('''| (press "b" to go back)                    |''')
    #     print('''|                                           |''')
    #     print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
    #     print()
    #     user_input = input("Input: ")
    #     print()
    #     if user_input == "1":
    #         print(self.contact_name)
    #         self.contact_name = input("Enter new name: ")
    #     elif user_input == "2":
    #         print(self.contact_phone)
    #         self.contact_phone = input("Enter new phone number: ")
    #     elif user_input == "3":
    #         print(self.contact_name)
    #         print(self.contact_phone)
    #         self.contact_name = input("Enter new name: ")
    #         self.contact_phone = input("Enter new phone number: ")
    #     elif user_input == "b":
    #         return None
    #     else:
    #         self.update_contact_info()
    #     self.confirm_contact_changes()

    def confirm_contact_changes(self):
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
            self.contact_confirmation()
        elif user_input == "2":
            pass

    def contact_confirmation(self):
        print()
        print(''' ___________________________________________''')
        print('''|                  NaN Air                  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| Contact information successfullly updated!|''')
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
            self.list_of_voyage()
        elif user_input == "2":
            self.list_of_contact_list
        elif user_input == "3":
            return None
        else:
            self.contact_confirmation()



####### UPDATE VOYAGE ##########

    def list_of_voyage(self):
        print("### listi af voyage prentast út og user velur 1, 2, 3 .....  ###")
        #Það sem user velur sendir það áfram í choose_employees()
        self.choose_employees()

    def choose_employees(self):
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
            pass
        elif user_input == "2":
            pass
        elif user_input == "b":
            return None
        else:
            self.choose_employees()
        self.replace_employee()
    
    def replace_employee(self):
        print("#### Prentast út þeir employees sem eru skráðir #####")###
        #User velur einhvern employee 
        self.find_new_employee()
    
    def find_new_employee(self):
        print("#### Listi af lausum employees prentast út ####") ###
        #User velur síðan nýjann employee
        self.confirm_voyage_changes()
    
    def confirm_voyage_changes(self):
        print("#### Prentast út ""Do you want to replace <emp1> with <emp2>?" ) ###
        print()
        print(''' ___________________________________________''')
        print('''|         NaN Air -                         |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (y) yes                                   |''')
        print('''| (n) no                                    |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        self.voyage_confirmation()
    
    def voyage_confirmation(self):
        print("Útskiptin prentast út") ####
        print()
        print(''' ___________________________________________''')
        print('''|                  NaN Air                  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| Voyage successfullly updated!             |''')
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
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        else:
            self.voyage_confirmation()

