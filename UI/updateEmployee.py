from Model.employee import Employee
#from LL.LLAPI import LLAPI

class UpdateEmployee():

    def __init__(self, llAPI_in):
        self.llAPI_in = llAPI_in
    
    def get_input(self):
        while True:
            self.employee_type = ""
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
                self.employee_type = "Pilot"
                pilot_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type) #Sækja lista af Pilots
                if self.show_list(pilot_list) == None:
                    return None
            elif user_input == "2":
                self.employee_type = "Cabincrew"
                fa_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type) #Sæka lista af FAs
                if self.show_list(fa_list) == None:
                    return None
            elif user_input == "b":
                return "Back to emp_m"
            else:
                continue


    def show_list(self, listOfEmployees):
        counter = 0
        for line in listOfEmployees:
            if counter < 1:
                for key in line.keys():
                    print(key, end="\t")
                counter += 1
        print()
        print("_____________________________________________________________________________")
        print()
        for line in listOfEmployees:
            for key,val in line.items():
                print(val, end="\t")
            print()
        print()
        self.id = input("Enter ID of employee: ")
        self.update_employee()



    def update_employee(self):
        while True:
            self.specific_emp = self.llAPI_in.getSpecificEmployee(self.id)
            print()
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            counter =1
            for key, val in self.specific_emp.items():
                print(" ({}) {}: {}".format(counter,key,val))
                counter += 1
            print('''                                            ''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Update: ")
            print()
            if user_input == "1":
                print("Can't change ID!") ###ATH
            elif user_input == "2":
                print("Can't change SSN!")
                self.ssn = self.ssn
            elif user_input == "3":
                print("Can't change name!")
                self.name = self.name
            elif user_input == "4":
                self.role = input("Enter role: ")
            elif user_input == "5":
                self.rank = input("Enter rank: ")
            elif user_input == "6":
                self.address = input("Enter address: ")
            elif user_input == "7":
                self.phone_no = input("Enter phone number: ")
            if self.employee_type == "Pilot":
                if user_input == "8":
                    self.license = input("Enter license: ")
                else:
                    pass 
            else:
                continue
            #if self.update_employee():
            #    self.display_info()


    def display_info(self):
        ''' Method thatn prints review of employee information. '''
        while True:
            print(''' ___________________________________________''')
            print('''|       NaN Air - Review information        |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            for key, val in self.specific_emp.items():
                print(" {}: {}".format(key,val))
            print('''                                             ''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Confirm                               |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            user_input = input("Input: ")
            if user_input == "1":
                    self.update_confirmation()
                    return None
            else:
                continue

    def update_confirmation(self):
        while True:
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
                continue
