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
        print("#####Prentast út listi frá data layer####") #####
        self.update_contact_info()

    def update_contact_info(self):
         # Velur hvort hann vilji update contact name, number eða bæði
        self.contact_name = ""
        self.contact_phone = ""
        print()
        print(''' ___________________________________________''')
        print('''|   NaN Air - update contact information    |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Contact name                          |''')
        print('''| (2) Contact phone number                  |''')
        print('''| (3) both                                  |''')
        print('''|                                           |''')
        print('''| (press "b" to go back)                    |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input("Input: ")
        print()
        if user_input == "1":
            print(self.contact_name)
            self.contact_name = input("Enter new name: ")
        elif user_input == "2":
            print(self.contact_phone)
            self.contact_phone = input("Enter new phone number: ")
        elif user_input == "3":
            print(self.contact_name)
            print(self.contact_phone)
            self.contact_name = input("Enter new name: ")
            self.contact_phone = input("Enter new phone number: ")
        elif user_input == "b":
            return None
        else:
            self.update_contact_info()
        self.confirm_contact_changes()

    def confirm_contact_changes(self):
        print()
        print(''' ___________________________________________''')
        print('''|   NaN Air - update contact information    |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| {:41} |'''.format(self.contact_name))
        print('''| {:41} |'''.format(self.contact_phone))
        print('''|                                           |''')
        print('''|                                           |''')
        print('''| Confirm changes?                          |''')
        print('''|                                           |''')
        print('''| (y) yes                                   |''')
        print('''| (n) no                                    |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input("Input: ")
        print()
        if user_input == "y":
            self.contact_confirmation()
        elif user_input == "n":
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

