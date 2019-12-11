#from LL.LLAPI import LLAPI
from Model.employee import Employee
import datetime

class GetEmployee():
    def __init__(self,llAPI_in):
        self.llAPI_in = llAPI_in

    def get_user_input(self):
        self.employee_type = ""
        while True:
            print()
            print(''' _________________________________________''')
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
                if self.print_specific_employee() == None:
                    return None
            elif user_input == "b":
                return "Back to emp_m"
            else:
                continue

    def get_list(self):
        self.employee_list = ""              #Fá lista af öllum pilots
        while True:
            print()
            print(''' _________________________________________''')
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
                    self.list_type = "all"
                    if self.pilot_list_sorting() == None:
                        continue
                elif self.employee_type == "Cabincrew":
                    self.list_type = "all"
                    fa_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type)
                    if self.print_list(fa_list) == None:
                        continue
                elif self.employee_type == "employees":
                    self.list_type = "all"
                    emp_list = self.llAPI_in.getEmployees()
                    if self.print_list(emp_list) == None:
                        continue
            elif user_input == "2":
                if self.employee_type == "Pilot":
                    self.list_type = "available"
                    if self.pilot_list_sorting() == None:
                        continue
                else:
                    self.list_type = "available"
                    self.year = int(input("Enter year: "))
                    self.month = int(input("Enter month: "))
                    self.day = int(input("Enter day: "))
                    self.date = datetime.date(self.year, self.month, self.day)
                    fa_list = self.llAPI_in.getAvailabiltyOfFAs(self.date, self.list_type)
                    if self.print_list(fa_list) == None:
                        continue
            elif user_input == "3":
                if self.employee_type == "Pilot":
                    self.list_type = "unavailable"
                    if self.pilot_list_sorting() == None:
                        continue
                else:
                    self.list_type = "unavailable"
                    self.year = int(input("Enter year: "))
                    self.month = int(input("Enter month: "))
                    self.day = int(input("Enter day: "))
                    self.date = datetime.date(self.year, self.month, self.day)
                    fa_list = self.llAPI_in.getAvailabiltyOfFAs(self.date, self.list_type)
                    if self.print_list(fa_list) == None:
                        continue
            elif user_input == "b":
                return None
            else:
                continue


    def pilot_list_sorting(self):
        while True:        #Kominn með réttann lista  (all, availablea eða unavailable)
            print()
            print(''' _________________________________________''')
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
                if self.list_type == "all":
                    pilot_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type)
                    self.print_list(pilot_list)
                else:
                    self.year = int(input("Enter year: "))
                    self.month = int(input("Enter month: "))
                    self.day = int(input("Enter day: "))
                    self.date = datetime.date(self.year, self.month, self.day)
                    pilot_list = self.llAPI_in.getAvailabilityOfPilots(self.date,self.list_type)
                    self.print_list(pilot_list)
                    
            elif user_input == "2":
                if self.list_type == "all":
                    pilot_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type)
                    self.sorted_plane_permit_list(pilot_list)
                else:
                    self.year = int(input("Enter year: "))
                    self.month = int(input("Enter month: "))
                    self.day = int(input("Enter day: "))
                    self.date = datetime.date(self.year, self.month, self.day)
                    pilot_list = self.llAPI_in.getAvailabilityOfPilots(self.date,self.list_type)
                    self.sorted_plane_permit_list(pilot_list)
            elif user_input == "3":
                if self.list_type == "all":
                    pilot_list = self.llAPI_in.getPilotsOrFAs(empType=self.employee_type)
                    self.sorted_by_specific_permit(pilot_list)
                else:
                    self.year = int(input("Enter year: "))
                    self.month = int(input("Enter month: "))
                    self.day = int(input("Enter day: "))
                    self.date = datetime.date(self.year, self.month, self.day)
                    pilot_list = self.llAPI_in.getAvailabilityOfPilots(self.date,self.list_type)
                    self.sorted_by_specific_permit(pilot_list)
            elif user_input == "b":
                return None 
            else:
                continue



    def sorted_plane_permit_list(self, listOfEmployees):
        ''' Prints out list of pilots sorted by plane permit'''
        print()
        planeTypeId = {}
        emp_name = ""
        for line in listOfEmployees:
            for key,val in line.items():
                if key == "Name":
                    emp_name = val
                elif key == "Licence":
                    if val not in planeTypeId:
                        planeTypeId[val] = emp_name
                    else:
                        planeTypeId[val] += "," + emp_name
            emp_name = ""
        for permit, names in planeTypeId.items(): #Getum líka látið user 
                                                  #velja hvaða permit hann vill skoða 
                                                  #og svo prenta út lista á pilots með það permit
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
        #plane_list = self.llAPI_in.getPlanes()
        permit_list = []
        chosen_permit = ""
        for line in listOfEmployees:
            for key, val in line.items():
                if key == "Licence":
                    if val not in permit_list:
                        permit_list.append(val)
        print()
        print(''' ___________________________________________''')
        print('''|         NaN Air - Choose permit           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        counter = 1
        for permit in permit_list:
            print("({}) {}".format(counter,permit))
            counter += 1
        print()
        user_input = int(input("Input: "))

        #Finna permit sem user valdi
        for index in range(len(permit_list) + 1):
            if index == user_input:
                chosen_permit = permit_list[index - 1]

        # Ath núna hvaða stm eru með þetta ákveðna permit
        emp_name = ""
        list_of_employees = []
        for line in listOfEmployees:
            for key,val in line.items():
                if key == "Name":
                    emp_name = val
                elif key == "Licence":
                    if val == chosen_permit:
                        list_of_employees.append(emp_name)
            emp_name = ""
        print()
        print(''' _________________''')
        print('''|   {:14}|'''.format(chosen_permit))
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        for name in list_of_employees:
            print(name)
        print("\n\n")
        print(input("Press enter to continue!"))



    def print_list(self, listOfEmployees): #C #Sorted by ID
        #line_index = 0
        #employees_list = self.llAPI_in.getEmployee()
        if listOfEmployees:
            counter = 0
            for line in listOfEmployees:
                if counter < 1:
                    for key in line.keys():
                        if key == "ID" or key == "SSN" or key == "Name":
                            print(key, end="\t  ")
                    counter += 1
            print()
            print("___________________________________________")
            print()
            for line in listOfEmployees:
                for key,val in line.items():
                    if key == "ID" or key == "SSN" or key == "Name":
                        print(val, end="\t")
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

########################### SPECIFIC EMPLOYEE ###########################


    def print_specific_employee(self):
        emp_list = self.llAPI_in.getEmployees()
        self.print_list(emp_list)
        print()
        specific_emp = self.llAPI_in.getSpecificEmployee(self.id)
        while True:
            print(''' ___________________________________________''')
            print('''|         NaN Air - Chosen employee         |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
            for key, val in specific_emp.items():
                if key == "SSN" or key == "Name":
                    print(" {}: {}".format(key,val))
            print("\n\n")
            print('''                                             ''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Get working schedule                  |''')
            print('''| (2) Get information                       |''')
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                self.get_working_schedule()
            elif user_input == "2":
                for key, val in specific_emp.items():
                    print(" {}: {}".format(key,val))
                print()
            elif user_input == "b":
                return None
            else:
                continue
    
    def get_working_schedule(self):
        pass
        #Enter year
        #Enter month
        #Enter day
        #Prenta út viku vaktaplan

