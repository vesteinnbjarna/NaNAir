#from LL.LLAPI import LLAPI
from Model.employee import Employee

class GetEmployee():

    def __init__(self,llAPI_in):
        self.llAPI_in = llAPI_in

    def get_user_input(self):
        self.employee_type = ""
        print()
        print(''' ___________________________________________''')
        print('''|           NaN Air -                       |''')
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
            if self.choose_list_sorting() == None:
                return None
        elif user_input == "2":
            self.employee_type = "cabincrew"
            if self.choose_list_sorting() == None:
                return None
        elif user_input == "3":
            self.employee_type = "employees"
            if self.choose_list_sorting() == None:
                return None
        elif user_input == "4":
            if self.specific_employee() == None:
                return None
        elif user_input == "b":
            return None
        else:
            self.get_user_input()


    def get_list(self):
        self.employee_list = ""              #Fá lista af öllum pilots
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
            self.employee_list = "all pilots"
            return self.employee_list
        elif user_input == "2":
            self.employee_list = "available pilots"
            return self.employee_list
        elif user_input == "3":
            self.employee_list = "unavailable pilots"
            return self.employee_list
        elif user_input == "b":
            self.get_user_input()
        else:
            self.get_list()


    def choose_list_sorting(self):
        self.employee_list = self.get_list()
        while self.employee_list != None:       #Kominn með réttann lista  (all, availablea eða unavailable)
            print()
            print(''' ___________________________________________''')
            print('''|           NaN Air -                       |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Get list sorted alpabetically         |''')
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
                user_input = input("Press enter to go back to home page")
            elif user_input == "2":
                pass
            elif user_input == "3":
                pass
            elif user_input == "b":
                self.get_list()
            else:
                self.choose_list_sorting()



########################### SPECIFIC EMPLOYEE ###############################

    def specific_list(self):
        #Ef þú velur specific employee þá geturu valið um að velja í lista af 
        #pilots eða cabincrew eða all employees
        self.specific_type = ""
        print()
        print(''' ___________________________________________''')
        print('''|           NaN Air -                       |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Get list of pilots                    |''')
        print('''| (2) Get list of cabincrew                 |''')
        print('''| (3) Get list of all employees             |''')
        print('''|                                           |''')
        print('''| (press "b" to go back)                    |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input("Input: ")
        print()
        if user_input == "1":
            self.specific_type = "pilots"
            return self.specific_type
        elif user_input == "2":
            self.specific_type = "cabincrew"
            return self.specific_type
        elif user_input == "3":
            self.specific_type = "all employees"
            return self.specific_type
        elif user_input == "b":
            self.get_user_input()
        else:
            self.specific_list()


    def specific_employee(self):
        self.specific_type = self.specific_list()
        #Prentar lista af lista sem user velur
        pass 
