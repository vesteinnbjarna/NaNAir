#from LL.LLAPI import LLAPI
from Model.employee import Employee

class GetEmployee():
    def __init__(self,llAPI_in):
        self.llAPI_in = llAPI_in

    def get_user_input(self):
        self.employee_type = ""
        while True:
            print()
            print(''' ___________________________________________''')
            print('''|                 NaN Air                   |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Pilots                                |''')
            print('''| (2) Cabincrew                             |''')
            print('''| (3) All employees                         |''')
            print('''| (4) Get data on specific employee         |''')
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                self.employee_type = "Pilot"
                if self.get_list() == None:
                    continue
            elif user_input == "2":
                self.employee_type = "Cabincrew"
                if self.get_list() == None:
                    continue
            elif user_input == "3":
                self.employee_type = "employees"
                if self.get_list() == None:
                    continue
            elif user_input == "4":
                self.employee_type = "Specific"
                if self.get_specific_employee() == None:
                    return None
            elif user_input == "b":
                return "Back to emp_m"
            else:
                continue

    def get_list(self):
        self.employee_list = ""              #Fá lista af öllum pilots
        while True:
            print()
            print(''' ___________________________________________''')
            print('''|           NaN Air -                       |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Get list of all {:22}|'''.format(self.employee_type + "s"))
            print('''| (2) Get list of available {:16}|'''.format(self.employee_type + "s"))
            print('''| (3) Get list of unavailable {:14}|'''.format(self.employee_type + "s"))
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Input: ")       #Eftir input að bera saman lista af all pilots við vinnutíma og sortera þá í available og unavailable
            print()
            if user_input == "1":
                if self.employee_type == "Pilot":
                    if self.pilot_list_sorting() == None:
                        continue
                elif self.employee_type == "Cabincrew":
                    fa_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type)
                    if self.print_list(fa_list) == None:
                        continue
                elif self.employee_type == "employees":
                    emp_list = self.llAPI_in.getEmployees()
                    if self.print_list(emp_list) == None:
                        continue
            elif user_input == "2":
                if self.employee_type == "Pilot":
                    if self.pilot_list_sorting() == None:
                        continue
                else:
                    if self.list_of_available == None:
                        continue
            elif user_input == "3":
                if self.employee_type == "Pilot":
                    if self.pilot_list_sorting() == None:
                        continue
                else:
                    if self.list_of_unavailable() == None:
                        continue
            elif user_input == "b":
                return None
            else:
                continue

    def pilot_list_sorting(self):
        while True:        #Kominn með réttann lista  (all, availablea eða unavailable)
            print()
            print(''' ___________________________________________''')
            print('''|         NaN Air - Choose sorting          |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Get list sorted by ID                 |''')
            print('''| (2) Get list sorted by plane permit       |''')
            print('''| (3) Get list of pilots with specific      |''')
            print('''|     permit                                |''')
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Input: ")       #Eftir input bera listann saman við plane permit eða pilots witf specific permit
            print()
            if user_input == "1":
                pilot_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type)
                self.print_list(pilot_list)
            elif user_input == "2":
                pass
            elif user_input == "3":
                pass
            elif user_input == "b":
                return None 
            else:
                continue

    def print_list(self, listOfEmployees): #C #Sorted by ID
        #line_index = 0
        #employees_list = self.llAPI_in.getEmployee()
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
                #line_index += 1
            print()
        print()
        if self.employee_type == "Specific":
            self.id = input("Enter employee ID: ")
            return self.id
        else:
            user_input = input("Press enter to go back")

    def list_sorted_by_permit(self): #B #Sorted in LL
        pass
    
    def list_specific_permit(self): #B #Filter in LL
        pass
    
    def list_of_available(): #A
        pass

    def list_of_unavailable(): #A
        pass

########################### SPECIFIC EMPLOYEE ###########################

    def get_specific_employee(self):
        emp_list = self.llAPI_in.getEmployees()
        self.print_list(emp_list)
        print()
        if self.print_specific_employee() == None:
            return None

    def print_specific_employee(self):
        while True:
            specific_emp = self.llAPI_in.getSpecificEmployee(self.id)
            print(''' ___________________________________________''')
            print('''|     NaN Air - Employee information        |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
            for key, val in specific_emp.items():
                print(" {}: {}".format(key,val))
            print('''                                             ''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Get information on another employee   |''')
            print('''| (2) Go back to home page                  |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Input: ")
            if user_input == "1":
                self.get_specific_employee()
            elif user_input == "2":
                return None
            else:
                continue






