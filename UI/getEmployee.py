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
                self.employee_type = "pilots"
                if self.get_list() == None:
                    continue
            elif user_input == "2":
                self.employee_type = "cabincrew"
                if self.get_list() == None:
                    continue
            elif user_input == "3":
                self.employee_type = "employees"
                if self.get_list() == None:
                    continue
            elif user_input == "4":
                pass
                #self.specific_emp_info() == None:
                 #   continue
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
            print('''| (1) Get list of all {:22}|'''.format(self.employee_type))
            print('''| (2) Get list of available {:16}|'''.format(self.employee_type))
            print('''| (3) Get list of unavailable {:14}|'''.format(self.employee_type))
            print('''|                                           |''')
            print('''| (press "b" to go back)                    |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Input: ")       #Eftir input að bera saman lista af all pilots við vinnutíma og sortera þá í available og unavailable
            print()
            if user_input == "1":
                if self.employee_type == "pilots":
                    if self.pilot_list_sorting() == None:
                        continue
                else:
                    if self.list_of_all() == None:
                        continue
            elif user_input == "2":
                if self.employee_type == "pilots":
                    if self.pilot_list_sorting() == None:
                        continue
                else:
                    if self.list_of_available == None:
                        continue
            elif user_input == "3":
                if self.employee_type == "pilots":
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
                self.list_of_all()
            elif user_input == "2":
                pass
            elif user_input == "3":
                pass
            elif user_input == "b":
                return None 
            else:
                continue

    def list_of_all(self): #C #Sorted by ID
        line_index = 0
        employees_list = self.llAPI_in.getEmployee()
        counter = 0
        for line in employees_list:
            if counter < 1:
                for key in line.keys():
                    print(key, end="\t")
                counter += 1
            else:
                print()
                break
        for line in employees_list:
            for key,val in line.items():
                print(val, end="\t")
                line_index += 1
            print()
        print()
        user_input = input("Press enter to go back")

    def list_sorted_by_permit(self): #B #Sorted in LL
        pass
    
    def list_specific_permit(self): #B #Filter in LL
        pass
    
    def list_of_available(): #A
        pass

    def list_of_unavailable(): #A
        pass

########################### SPECIFIC EMPLOYEE ###############################

    def specific_emp_info(self):
        #Ef þú velur specific employee þá geturu valið um að velja í lista af 
        #pilots eða cabincrew eða all employees
        list_of_all()
        chosen_emp = input("Enter ID of employee: ")
        if True: 
            return None
        else:
            print("Employee not found!")
            continue


    def specific_employee(self):
        self.specific_type = self.specific_list()
        #Prentar lista af lista sem user velur
        pass 
