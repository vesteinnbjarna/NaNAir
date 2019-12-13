#from LL.LLAPI import LLAPI
from Model.employee import Employee
import datetime

class GetEmployee():
    def __init__(self,llAPI_in):
        self.llAPI_in = llAPI_in
        self.list_type = 'All'

    def get_user_input(self):
        ''' Method that gets user input and determines employee type,
            stores it and calls appropriate method. '''
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
                self.employee_type = "Employees"
                if self.get_list() == None:
                    continue
            elif user_input == "4":
                self.employee_type = "Specific"
                self.list_type = ''
                if self.print_specific_employee() == None:
                    return None
            elif user_input == "b":
                return "Back to emp_m"
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue        #if invalid input, continue.

    def get_list(self):
        ''' Method that gets what type of list user wants,
            stores it and calls the appropriate function that
            returns right list. '''
        self.employee_list = ""
        while True:
            print()
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Get list of all {:22}|'''.format(self.employee_type + "s"))
            print('''| (2) Get list of available {:16}|'''.format(self.employee_type + "s"))
            print('''| (3) Get list of unavailable {:14}|'''.format(self.employee_type + "s"))
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Input: ")
            print()

            #Check input, then check employee type.
            #If employee type pilot then we call pilot_list_sorting method and 
            #ask for another input.
            if user_input == "1":
                if self.employee_type == "Pilot":
                    self.list_type = "All"
                    if self.pilot_list_sorting() == None:
                        continue
                elif self.employee_type == "Cabincrew":
                    self.list_type = "All"
                    fa_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type)
                    if self.print_list(fa_list) == None:
                        continue
                elif self.employee_type == "Employees":
                    self.list_type = "All"
                    emp_list = self.llAPI_in.getEmployees()
                    if self.print_list(emp_list) == None:
                        continue

            #If user chooses available or unavailable, then we ask for
            #what date user wants to check.
            elif user_input == "2":
                if self.employee_type == "Pilot":
                    self.list_type = "Available"
                    if self.pilot_list_sorting() == None:
                        continue
                else:
                    self.list_type = "Available"
                    self.date = self.get_date_input()
                    if self.employee_type == "Cabincrew":
                        fa_list = self.llAPI_in.getAvailabiltyOfFAs(self.date, self.list_type)
                        if self.print_list(fa_list) == None:
                            continue
                    elif self.employee_type == "Employees":
                        allEmp_list = self.llAPI_in.getAvailabilityOfAll(self.date, self.list_type)
                        if self.print_list(allEmp_list) == None:
                            continue 

            elif user_input == "3":
                if self.employee_type == "Pilot":
                    self.list_type = "Unavailable"
                    if self.pilot_list_sorting() == None:
                        continue
                else:
                    self.list_type = "Unavailable"
                    self.date = self.get_date_input()
                    if self.employee_type == "Cabincrew":
                        fa_list = self.llAPI_in.getAvailabiltyOfFAs(self.date, self.list_type)
                        if self.print_list(fa_list) == None:
                            continue
                    elif self.employee_type == "Employees":
                        allEmp_list = self.llAPI_in.getAvailabilityOfAll(self.date, self.list_type)
                        if self.print_list(allEmp_list) == None:
                            continue

            elif user_input == "b":
                return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue        #if invalid input, continue.


    def pilot_list_sorting(self):
        ''' If employee type is pilot then we call this method.
            User can choose sorting of list. '''
        while True:        
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
            user_input = input("Input: ")   
            print()

            #Check input and call appropriate class and method to get correct list

            if user_input == "1":
                if self.list_type == "All":
                    pilot_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type)
                    self.print_list(pilot_list)
                else:
                    self.date = self.get_date_input()
                    pilot_list = self.llAPI_in.getAvailabilityOfPilots(self.date,self.list_type)
                    if self.list_type == "Unavailable":
                        self.print_list(pilot_list)
                    elif self.list_type == "Available":
                        self.print_list(pilot_list)
                    
            elif user_input == "2":
                if self.list_type == "All":
                    pilot_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type)
                    self.sorted_plane_permit_list(pilot_list)
                else:
                    self.date = self.get_date_input()
                    pilot_list = self.llAPI_in.getAvailabilityOfPilots(self.date,self.list_type)
                    self.sorted_plane_permit_list(pilot_list)

            elif user_input == "3":
                if self.list_type == "All":
                    pilot_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type)
                    self.sorted_by_specific_permit(pilot_list)
                else:
                    self.date = self.get_date_input()
                    pilot_list = self.llAPI_in.getAvailabilityOfPilots(self.date,self.list_type)
                    self.sorted_by_specific_permit(pilot_list)

            elif user_input == "b":
                return None 
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue



    def sorted_plane_permit_list(self, listOfEmployees):
        ''' Prints out list of pilots sorted by plane permit'''
        print()
        planeTypeId = {}
        emp_name = ""
        for line in listOfEmployees:
            if len(line) == 1:
                pass
            else:
                for key,val in line.items():
                    if key == "Name":
                        emp_name = val
                    elif key == "Licence":
                        if val not in planeTypeId:
                            planeTypeId[val] = emp_name
                        else:
                            planeTypeId[val] += "," + emp_name
            emp_name = ""
        if self.list_type == "Available" or self.list_type == "Unavailable":
            print()
            print(''' ___________________________________________''')
            print('''|   {:>11} employees on {:15}|'''.format(self.list_type,str(self.date)))
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        for permit, names in planeTypeId.items(): 
            print()
            print(''' _________________''')
            print('''|   {:14}|'''.format(permit))
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            names_list = names.split(",")
            
            for name in sorted(names_list):
                print("{}".format(name))
        print("\n\n")
        print(input("Press enter to continue!"))


    def sorted_by_specific_permit(self, listOfEmployees):
        plane_list = self.llAPI_in.getPlanes()
        all_employees = self.llAPI_in.getEmployees()
        permit_list = []
        chosen_permit = ""
        # Print out list of permits and let user choose specific permit
        for line in plane_list:
            for key, val in line.items():
                if key == "planeTypeId":
                    if val not in permit_list:
                        permit_list.append(val)
        for line in all_employees:
            for key, val in line.items():
                if key == "Licence":
                    if val != "N/A":
                        if val not in permit_list:
                            permit_list.append(val)

        valid_input = False
        while valid_input == False:
            print()
            print(''' ___________________________________________''')
            print('''|         NaN Air - Choose permit           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            counter = 1
            for permit in permit_list:
                print("({}) {}".format(counter,permit))
                counter += 1
            print()

            user_input = input("Input: ")

            try:
                user_input = int(user_input)

                if user_input in range(1, len(permit_list)+1):
                    valid_input = True
                else:
                    print()
                    print(''' _________________________''')
                    print('''|Invalid input! try again.|''')
                    print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            except ValueError:
                print()
                print(''' _________________________''')
                print('''|Invalid input! try again.|''')
                print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')


        # Find what permit user chose
        for index in range(len(permit_list) + 1):
            if index == user_input:
                chosen_permit = permit_list[index - 1]

        # Print out a list of pilots with the permit that user chose
        emp_name = ""
        list_of_employees = []
        for line in listOfEmployees:
            if len(line) == 1:
                pass
            else:
                for key,val in line.items():
                    if key == "Name":
                        emp_name = val
                    elif key == "Licence":
                        if val == chosen_permit:
                            list_of_employees.append(emp_name)
            emp_name = ""

        if self.list_type == "Available" or self.list_type == "Unavailable":
            print()
            print(''' ___________________________________________''')
            print('''|   {:>11} employees on {:15}|'''.format(self.list_type,str(self.date)))
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        print(''' _________________''')
        print('''|   {:14}|'''.format(chosen_permit))
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        if len(list_of_employees) == 0:
            print("!!! LAZY EMPLOYEE ALERT !!!")
            print()
            print("No employee with specific permit working.")
            print()
        else:
            for name in sorted(list_of_employees):
                print(name)
        print("\n\n")
        print(input("Press enter to continue!"))
        

    def print_list(self, listOfEmployees):
        while True:
        #Sorted by ID
            if self.list_type == "Available" or self.list_type == "Unavailable":
                print()
                print(''' ___________________________________________''')
                print('''|   {:>11} employees on {:15}|'''.format(self.list_type,str(self.date)))
                print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
                print()
            if listOfEmployees:
                counter = 0
                for line in listOfEmployees:
                    if counter < 1:
                        for key in line.keys():
                            if key == "ID":
                                print("{:5}".format(key), end=" ")
                            elif key == "SSN":
                                print("{:15}".format(key), end=" ")
                            elif key == "Name":
                                print("{:25}".format(key), end=" ")
                            elif key == "Role":
                                print("{:15}".format(key), end=" ")
                        if self.list_type == "Unavailable":
                            print("{:15}".format("Destination"))
                            print("__"*40)
                        else:
                            print("\n____________________________________________________________")
                        counter += 1
        
                print()
                #If unavailable we want to print out destination
                if self.list_type == "Unavailable":
                    for line in listOfEmployees:
                        if len(line) == 1:
                            for dest in line:
                                print("{:15}".format(dest))
                        else:
                            for key,val in line.items():
                                if key == "ID":
                                    print("\n{:5}".format(val), end=" ")
                                elif key == "SSN":
                                    print("{:15}".format(val), end=" ")
                                elif key == "Name":
                                    print("{:25}".format(val), end=" ")
                                elif key == "Role":
                                    print("{:15}".format(val), end=" ")
                            
                else:
                    for line in listOfEmployees:
                        for key,val in line.items():
                            if key == "ID":
                                print("{:5}".format(val), end=" ")
                            elif key == "SSN":
                                print("{:15}".format(val), end=" ")
                            elif key == "Name":
                                print("{:25}".format(val), end=" ")
                            elif key == "Role":
                                print("{:15}".format(val), end=" ")
                        print()
                print()
                if self.employee_type == "Specific":
                    self.id = input("Enter employee ID: ")
                    return self.id
            else:
                print()
                print("No employees found")
            print()
            input("Press enter to continue")
            return None 




########################### SPECIFIC EMPLOYEE ###########################
    
    
    def print_specific_employee(self):
        while True:
            emp_list = self.llAPI_in.getEmployees()
            self.print_list(emp_list)
            print()
            self.specific_emp = self.llAPI_in.getSpecificEmployee(self.id)
            #check if input of ID is valid, if not valid then continue
            if self.specific_emp == None:
                input("Press enter to input another ID!")
                print()
                continue
            else:
                break
        # Print list of employees and let user choose a specific employee
        while True:
            self.name = ""
            print(''' ___________________________________________''')
            print('''|         NaN Air - Chosen employee         |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
            print()
            for key, val in self.specific_emp.items():
                if key == "SSN":
                    print(" {}: {}".format(key,val))
                elif key == "Name":
                    self.name = val
                    print(" {}: {}".format(key,val))
            print()
            print('''                                             ''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Get working schedule                  |''')
            print('''| (2) Get information                       |''')
            print('''|                                           |''')
            print('''| (3) Back to homepage                      |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                self.get_working_schedule()
            elif user_input == "2":
                for key, val in self.specific_emp.items():
                    print(" {}: {}".format(key,val))
                print()
                input("Press enter to go back")
                continue
            elif user_input == "3":
                return None
            else:
                print()
                print("Invalid input!")
                print()
                input("Press enter to try again :-)")                    
                continue
    
    def get_working_schedule(self):
        self.date_input = self.get_date_input()
        voyage_list_week = self.llAPI_in.getVoyagesWeek(self.date_input)
        print(''' ___________________________________________''')
        print('''|      {}: {:27}|'''.format("Employee",self.name))
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
        print()
        print("{:30}{:30}{:30}".format("Destination", "Departure", "Arrival"))
        print("__"*40)
        working = False
        for line in voyage_list_week:
            if line['Captain'] == self.specific_emp['SSN'] or line['Copilot'] == self.specific_emp['SSN'] or \
                line['FSM'] == self.specific_emp['SSN'] or line['FA1'] == self.specific_emp['SSN'] or \
                line['FA2'] == self.specific_emp['SSN']:
                print()
                working = True
                for key, val in line.items():
                    if key == "Destination":
                        print("{:30}".format(val), end="")
                    elif key == "Departure":
                        val = val.replace("T", " ")
                        print("{:30}".format(val), end="")
                    elif key == "Arrival":
                        val = val.replace("T", " ")
                        print("{:30}".format(str(val)), end="")
                print()
            elif working == False:
                print()
                print("{:^70}".format("!!! LAZY EMPLOYEE ALERT !!! "))
                print()
                print("{:^70}".format("Employee not working this week. "))
                break
        print("\n\n")
        input("Press enter to continue")


    def get_date_input(self):
        ''' Method that gets date input and check if valid,
            and returns date in datetime format. '''
        while True:
            try:
                self.year = int(input("Enter year (yyyy): "))
                self.month = int(input("Enter month (mm): "))
                self.day = int(input("Enter day (dd): "))
            except ValueError:
                print(''' _________________________''')
                print('''|Invalid input! try again.|''')
                print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')                
                continue
            print("\n\n")
            try:
                self.date = datetime.date(self.year, self.month, self.day)
                return self.date
            except ValueError:
                print(''' _________________________''')
                print('''|Invalid date! try again.|''')
                print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')                
                continue
            