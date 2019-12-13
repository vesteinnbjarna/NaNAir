from Model.employee import Employee
from LL.LLAPI import LLAPI

class CreateEmployee():
    def __init__(self, llAPI_in):
        self.llAPI_in = llAPI_in

    def get_role(self):
        ''' Returns role of new employee'''
        while True:
            self.role = ""
            print(''' ___________________________________________''')
            print('''|           NaN Air - Select role           |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Pilot                                 |''')
            print('''| (2) Cabincrew                             |''')
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            if user_input == "1":
                self.role = "Pilot"
                return self.role
            elif user_input == "2":
                self.role = "Cabincrew"
                return self.role
            elif user_input == "b":
                return "Back to emp_m"      #goes back to employee management class
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue

    def get_employee_info(self):
        ''' Method that gets role from get_role method and returns input from user whether
        pilot or cabincrew'''
        self.role = self.get_role()
        if self.role != "Back to emp_m":                            #if user enters back in previous method it 
            print(' _________________________________________')     #will not ask for input and goes back to emp_m
            print("| NaN Air - Enter employee information    |")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
            
            invalid_input = True
            #Ask for SSN and check if input is valid.
            while invalid_input == True:
                print()
                self.ssn = input("Enter SSN: ")
                if len(self.ssn) == 10:
                    try:
                        for char in self.ssn:
                            int(char)
                        #self.ssn = int(self.ssn)
                        invalid_input = False
                    except:
                        print()
                        print("Invalid SSN! Intigers only allowed!")
                        print("Try again!")
                        continue
                else:
                    print()
                    print("SSN must be 10 digits")
                    continue

            self.name = input("Enter name: ")
            self.rank = input("Enter rank: ")
            self.address = input("Enter address: ")

            #Ask for Phone number and check if input is valid.
            invalid_input = True
            while invalid_input == True:
                self.phone_no = input("Enter phone number: ")
                if len(self.phone_no) == 7:
                    try:
                        self.phone_no = int(self.phone_no)
                        invalid_input = False
                    except:
                        print()
                        print("Invalid phone number! Intigers only allowed!")
                        print("Try again!")
                        print()
                        continue
                else:
                    print()
                    print("Phone number must be 7 digits")
                    print()
                    continue

            #get licence if pilot
            if self.role == "Pilot":
                self.license = input("Enter license: ")
            #cabincrew
            else:                               
                self.license = "N/A"
            if self.display_info() == None:
                return None
        else:
            return "Back to emp_m"


    def display_info(self):
        ''' Method thatn prints review of employee information. '''
        while True:
            print(''' ___________________________________________''')
            print('''|       NaN Air - Review information        |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| SSN: {:<37}|'''.format(self.ssn))
            print('''| Name: {:<36}|'''.format(self.name))
            print('''| Role: {:<36}|'''.format(self.role))
            print('''| Rank: {:<36}|'''.format(self.rank))
            print('''| Address: {:<33}|'''.format(self.address))
            print('''| Phone number: {:<28}|'''.format(self.phone_no))
            print('''| License: {:<33}|'''.format(self.license))
            print('''|                                           |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Confirm                               |''')
            print('''| (2) Edit                                  |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            if user_input == "1":
                if self.create_employee():
                    self.print_confirmation()
                    return None
                else:
                    print('try again')
                    return None
            elif user_input == "2":
                if self.display_info_to_edit() == None:
                    return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                     
                continue

    def display_info_to_edit(self):  
        ''' Method that asks user what information to edit. '''
        while True:
            print(''' ___________________________________________''')
            print('''|        NaN Air - Edit information         |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) SSN: {:<33}|'''.format(self.ssn))
            print('''| (2) Name: {:<32}|'''.format(self.name))
            print('''| (3) Role: {:<32}|'''.format(self.role))
            print('''| (4) Rank: {:<32}|'''.format(self.rank))
            print('''| (5) Address: {:<29}|'''.format(self.address))
            print('''| (6) Phone number: {:<24}|'''.format(self.phone_no))
            if self.role == "Pilot":
                print('''| (7) License: {:<29}|'''.format(self.license))
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
            user_input = input("Edit selection: ")
            print()
            if user_input == "1":
                invalid_input = True
                while invalid_input == True:
                    print()
                    self.ssn = input("Enter SSN: ")
                    if len(self.ssn) == 10:
                        try:
                            self.ssn = int(self.ssn)
                            invalid_input = False
                        except:
                            print()
                            print("Invalid SSN! Intigers only allowed!")
                            print("Try again!")
                            continue
                    else:
                        print()
                        print("SSN must be 10 digits")
                        continue
                if self.display_info() == None:
                    return None
            elif user_input == "2":
                self.name = input("Enter name: ")
                if self.display_info() == None:
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
                    return None
            elif user_input == "6":
                invalid_input = True
                while invalid_input == True:
                        self.phone_no = input("Enter phone number: ")
                        if len(self.phone_no) == 7:
                            try:
                                self.phone_no = int(self.phone_no)
                                invalid_input = False
                            except:
                                print()
                                print("Invalid phone number! Intigers only allowed!")
                                print("Try again!")
                                print()
                                continue
                        else:
                            print()
                            print("Phone number must be 7 digits")
                            print()
                            continue
                if self.display_info() == None:
                    return None
            if self.role == "Pilot":
                if user_input == "7":
                    self.license = input("Enter license: ")
                    if self.display_info() == None:
                        return None          
                else:
                    return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue



    def print_confirmation(self):
        ''' Method that prints confirmation of employee creation. '''
        while True:
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| Employee successfullly created!           |''')
            print('''|                                           |''')
            print('''|                  __|__                    |''')
            print('''|              ---@-(")-@---                |''')
            print('''|                                           |''')
            print('''|                                           |''')
            print('''| (1) Create another employee               |''')
            print('''| (2) Go back to home page                  |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
            user_input = input("Input: ")
            if user_input == "1":
                if self.get_employee_info() == None:
                    return None
            elif user_input == "2":
                return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue

    def create_employee(self):
        if self.role == "Pilot":
            self.employee = Employee(self.ssn, self.name, self.role, self.rank, \
                self.address, self.phone_no, self.license)
        else:
            self.employee = Employee(self.ssn, self.name, self.role, self.rank, \
                self.address, self.phone_no, self.license)
        self.llAPI_in.createEmployee(self.employee)
        return self.employee


