from Model.employee import Employee

class UpdateEmployee():

    def __init__(self, llAPI_in):
        self.llAPI_in = llAPI_in
    

    def get_input(self):
        ''' Get employee type user wants to update. '''
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
                pilot_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type) #Get list of pilots.
                if self.show_list(pilot_list) == None:
                    return None

            elif user_input == "2":
                self.employee_type = "Cabincrew"
                fa_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type) #Get list of FAs.
                if self.show_list(fa_list) == None:
                    return None

            elif user_input == "b":
                return "Back to emp_m"

            else:
                continue


    def show_list(self, listOfEmployees):
        ''' Method that prints out list of chosen employees, and gets ID of employee
            that user wants to update. '''
        while True:
            self.ID_list = []
            header_list = self.llAPI_in.getEmployeeHeader(listOfEmployees)
            value_list = self.llAPI_in.getEmployeeValue(listOfEmployees)
            print("{:<10}{:<20}{:<30}{:<20}".format(header_list[0],header_list[1],header_list[2],header_list[4]))
            print("__"*42)

            for line in value_list:
                print("{:<10}{:<20}{:<30}{:<20}".format(line[0],line[1],line[2],line[4]))
                self.ID_list.append(line[0])
            print()
            self.id = input("Enter ID of employee: ") # can also be used to index line in the csv file
            self.specific_emp = self.llAPI_in.getChosenEmployee(self.ID_list, self.id)
            self.line_index = self.id

            print()
            
            if self.update_employee() == None:

                if self.specific_emp == None:
                    input("Press enter to try again!")
                    continue

                else:
                    if self.update_employee() == None:
                        return None

                return None

    def update_employee(self):
        ''' Method that prints out information about chosen employee and
            asks user what information he wants to update. '''
        while True:
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
                print("Can't change ID!")
                continue

            elif user_input == "2":
                print("Can't change SSN!")
                continue

            elif user_input == "3":
                print("Can't change name!")
                continue

            elif user_input == "4":
                self.role = input("Enter role: ")
                self.updated_info = self.role
                self.row_index = 3

            elif user_input == "5":
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
                self.email = input("Enter email: ")
                self.updated_info = self.email
                self.row_index = 8
 
            else:
                continue

            if self.update_csv() == None:
                return None       
       

    def display_info(self):
        ''' Method that prints review of employee information after update. '''
        updated_emp = self.llAPI_in.getSpecificEmployee(self.id) 
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
                self.llAPI_in.updateEmployee(self.line_index,self.row_index,self.updated_info)

                if self.update_confirmation() == None:
                    return None
            else:
                continue


    def update_confirmation(self):
        ''' Method that prints out confirmation of update. '''
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


    def update_csv(self):
        self.llAPI_in.updateEmployee(self.id,self.row_index,self.updated_info)
        if self.display_info() == None:
            return None