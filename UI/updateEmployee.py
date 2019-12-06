from Model.employee import Employee
#from LL.LLAPI import LLAPI

class UpdateEmployee():

    def __init__(self, llAPI_in):
        self.llAPI_in = llAPI_in
    
    def get_input(self):
        print()
        print(''' ___________________________________________''')
        print('''|        NaN Air - Update Employee          |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Update pilot                          |''')
        print('''| (2) Update cabincrew                      |''')
        print('''|                                           |''')
        print('''| (press "b" to go back)                    |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input("Input: ")
        print()
        if user_input == "1":
            if self.list_of_employees() == None:
                return None
        elif user_input == "2":
            if self.list_of_employees() == None:
                return None
        elif user_input == "b":
            return None
        else:
            self.get_input()

    def list_of_employees(self):
        #Senda uppl á data layer um að fá lista af annaðhvort pilots eða CC
        print("#####Prentast út listi frá data layer####") #####

    def update_employee(self):
        print()
        print(''' ___________________________________________''')
        print('''|        NaN Air - Edit information         |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) SSN: {:33}|'''.format(self.ssn))
        print('''| (2) Name: {:32}|'''.format(self.name))
        print('''| (3) Role: {:32}|'''.format(self.role))
        print('''| (4) Rank: {:32}|'''.format(self.rank))
        print('''| (5) Address: {:29}|'''.format(self.address))
        print('''| (6) Phone number: {:24}|'''.format(self.phone_no))
        if self.role == "Pilot":
            print('''| (7) License: {:29}|'''.format(self.license))
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input("Input: ")
        print()
        if user_input == "1":
            self.ssn = input("Enter SSN: ")
            self.display_info()
        elif user_input == "2":
            self.name = input("Enter name: ")
            self.display_info()
        elif user_input == "3":
            self.role = input("Enter role: ")
            self.display_info()
        elif user_input == "4":
            self.rank = input("Enter rank: ")
            self.display_info()
        elif user_input == "5":
            self.address = input("Enter address: ")
            self.display_info()
        elif user_input == "6":
            self.phone_no = input("Enter phone number: ")
            self.display_info()
        if self.role == "Pilot":
            if user_input == "7":
                self.license = input("Enter license: ")
                self.display_info()
            else:
                pass #self.display_info_to_edit()
        else:
            pass #self.display_info_to_edit()"""

    def update_confirmation(self):
        print()
        print(''' ___________________________________________''')
        print('''|                  NaN Air                  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''|          Successfullly updated!           |''')
        print('''|                                           |''')
        print('''| (1) Update more information               |''')
        print('''| (2) Update another employee               |''')
        print('''|                                           |''')
        print('''| (3) Back to home page                     |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
        print()
        user_input = input("Input: ")
        print()
        if user_input == "1":
            self.update_employee()
        elif user_input == "2":
            self.get_input()
        elif user_input == "3":
            return None
        else:
            self.update_confirmation()


