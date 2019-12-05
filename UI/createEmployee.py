from Model.employee import Employee

class CreateEmployee():
    def get_role(self):
        print()
        print(''' ___________________________________________''')
        print('''|           NaN Air - Select role           |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Pilot                                 |''')
        print('''| (2) Cabincrew                             |''')
        print('''|                                           |''')
        print('''| (press "b" to go back)                    |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input("Input: ")
        if user_input != "b":
            print()
            print(' _________________________________________')
            print("|  NaN Air - Enter employee information   |")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
            print()
            self.role = ""
            if user_input == "1":
                self.role = "Pilot"
            elif user_input == "2":
                self.role = "Cabincrew"
            return self.role
        return None


    def get_employee_info(self):
        self.role = self.get_role()
        if self.role:
            self.ssn = input("Enter SSN: ")
            self.name = input("Enter name: ")
            self.rank = input("Enter rank: ")
            self.address = input("Enter address: ")
            self.phone_no = input("Enter phone number: ")
            if self.role == "Pilot":
                self.license = input("Enter license: ")
            else:                               # Cabincrew
                self.license = "N/A"
            if self.display_info() == None:
                return None


    def display_info(self):
        print()
        print(''' ___________________________________________''')
        print('''|       NaN Air - Review information        |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| SSN: {:37}|'''.format(self.ssn))
        print('''| Name: {:36}|'''.format(self.name))
        print('''| Role: {:36}|'''.format(self.role))
        print('''| Rank: {:36}|'''.format(self.rank))
        print('''| Address: {:33}|'''.format(self.address))
        print('''| Phone number: {:28}|'''.format(self.phone_no))
        print('''| License: {:33}|'''.format(self.license))
        print('''|                                           |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Confirm                               |''')
        print('''| (2) Edit                                  |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input("Input: ")
        print()
        if user_input == "1":
            if self.print_confirmation():
                self.print_confirmation()
                self.employee = self.create_employee()
            else:
                return None
        elif user_input == "2":
            self.display_info_to_edit()

    def display_info_to_edit(self):
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
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
        print()
        user_input = input("Edit selection: ")
        print()
        if user_input == "1":
            self.ssn = input("Enter SSN: ")
        elif user_input == "2":
            self.name = input("Enter name: ")
        elif user_input == "3":
            self.role = self.get_role()
        elif user_input == "4":
            self.rank = input("Enter rank: ")
        elif user_input == "5":
            self.address = input("Enter address: ")
        elif user_input == "6":
            self.phone_no = input("Enter phone number: ")
        if self.role == "Pilot":
            if user_input == "7":
                self.license = input("Enter license: ")
        self.display_info()

    def print_confirmation(self):
        print(''' ___________________________________________''')
        print('''|                  NaN Air                  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| Empployee successfullly created!          |''')
        print('''|                                           |''')
        print('''| (1) Create another employee               |''')
        print('''| (2) Go back to home page                  |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
        print()
        user_input = input("Input: ")
        print()
        if user_input == "1":
            self.get_employee_info()
        elif user_input == "2":
            return None

    def create_employee(self):
        self.employee = Employee(self.ssn, self.name, self.role, self.rank, \
            self.address, self.phone_no, self.license)
        return self.employee