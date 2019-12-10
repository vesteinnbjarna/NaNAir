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
        self.id = input("Enter ID of employee: ") # can also be used to index line in the csv file
        self.update_employee()



    def update_employee(self):
        while True:
            self.specific_emp = self.llAPI_in.getSpecificEmployee(self.id)
            print()
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            counter = 1
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
            elif user_input == "3":
                print("Can't change name!")
            elif user_input == "4":
                self.role = input("Enter role: ")
                self.updated_info = self.role
                self.row_index = 3
            elif user_input == "5": # ATH er held ég ekki í csv
                self.rank = input("Enter rank: ")
                self.updated_info = self.rank
                self.row_index = 4
            elif user_input == "6":
                if self.employee_type != 'Pilot':
                    print("Not a pilot!")
                else:
                    self.license = input("Enter license: ")
                    self.updated_info = self.license
                    self.row_index = 5
            elif user_input == "7":
                self.address = input("Enter address: ")
                self.updated_info = self.address
                self.row_index = 6
           
            elif user_input == "8":
                self.phone_no = input("Enter phone number: ")
                self.updated_info = self.phone_no
                self.row_index = 7

            elif user_input == "9":
                self.email = input("Enter email")
                self.updated_info = self.email
                self.row_index = 8
 
            else:
                continue

            self.update_csv()   # ATH hérna erum við að breyta csv!!  
                                # þurfum mögulega að finna betri
                                # leið til að gera þetta!

    def update_csv(self):
        self.llAPI_in.updateEmployee(self.id,self.row_index,self.updated_info)
        self.display_info()
        # ATH að self.id virkar alveg eins og index á línuna sem
        # við viljum breyta :)

    def display_info(self):
        ''' Method thatn prints review of employee information. '''
        updated_emp = self.llAPI_in.getSpecificEmployee(self.id) #Sæki réttar update-aðar upplýsingar til að prenta út.
        while True:
            print(''' ___________________________________________''')
            print('''|       NaN Air - Review information        |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            for key, val in updated_emp.items():  
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
