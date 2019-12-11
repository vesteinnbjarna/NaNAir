#from IO.IOAPI import IOAPI

class EmployeeLL ():
    def __init__ (self, ioAPI):
        self.__ioAPI = ioAPI

    def createEmployee (self,employee):
        self.__ioAPI.storeEmployeeToFile(employee)
        
    
    def updateEmployee (self,line_index, row_index, updated_info):
        self.__ioAPI.updateEmployeeInFile(line_index, row_index, updated_info)

    def getEmployees(self):
        return self.__ioAPI.loadEmployeesFromFile()
    
    def getEmployeeHeader(self,employee_list):
        header_list = []
        counter = 0
        for line in employee_list:
            if counter < 1:
                for k,v in line.items():
                    header_list.append(k)
                counter += 1
            else:
                return header_list


    def getEmployeeValue(self,employee_list):
        value_list = []
        for line in employee_list:
            h_id = line["ID"]
            h_ssn = line["SSN"]
            h_name = line["Name"]
            h_role = line["Role"]
            h_rank = line["Rank"]
            h_lice = line["Licence"]
            h_addr = line["Address"]
            h_nr = line["Phonenumber"]
            h_email = line["Email"]
            value_list.append([h_id,h_ssn,h_name,h_role,h_rank,h_lice,h_addr,h_nr,h_email])       
        return value_list

    def getPilotsOrFAs(self,empType):
        list_of_employees = self.__ioAPI.loadEmployeesFromFile()
        listOfPilots = []
        listOfFAs = []
        if empType == "Pilot":
            for line in list_of_employees:
                for key,val in line.items():
                    if key == "Role":
                        if val == empType:
                            listOfPilots.append(line)
            return listOfPilots
        elif empType == "Cabincrew":
            for line in list_of_employees:
                for key,val in line.items():
                    if key == "Role":
                        if val == empType:
                            listOfFAs.append(line)
            return listOfFAs

    def getSpecificEmployee(self, emp_id):
        list_of_employees = self.__ioAPI.loadEmployeesFromFile()
        ID_list = []
        for line in list_of_employees:
            ID_list.append(line["ID"])
        if int(emp_id) not in range(1, len(ID_list)+1):
            print("ID not found!")
            return None
        else:
            for line in list_of_employees:
                if line['ID'] == emp_id:
                    return line
        

    def getAvailabiltyOfPilots(self, date, listType):
        ''' Returns a list of either available or unavailable pilots. '''
        list_of_pilots = self.getPilotsOrFAs("Pilot")
        list_of_voyages = self.__ioAPI.loadVoyagesFromFile()
        list_of_voyages_on_date = []
        # Creating a list of voyages on chosen date so we can check availablity of pilots.
        for voyage in list_of_voyages:
            if voyage['Departure'][:10] == str(date):
                list_of_voyages_on_date.append(voyage)
        list_of_available_pilots = []
        list_of_unavailable_pilots = []
        for pilot in list_of_pilots:
            for voyage in list_of_voyages_on_date:
                if voyage['Captain'] != pilot['SSN'] and voyage['Copilot'] != pilot['SSN']:
                    if pilot not in list_of_available_pilots:
                        list_of_available_pilots.append(pilot)
                else:
                    if pilot not in list_of_unavailable_pilots:
                        list_of_unavailable_pilots.append(pilot)
        if not list_of_voyages_on_date: # If no voyage on date -> all employees are available
            return list_of_pilots
        elif listType == "Available":
            return list_of_available_pilots
        elif listType == "Unavailable":
            return list_of_unavailable_pilots

    def getAvailabiltyOfFAs(self, date, listType):
        list_of_FAs = self.getPilotsOrFAs("Cabincrew")
        list_of_voyages = self.__ioAPI.loadVoyagesFromFile()
        list_of_voyages_on_date = []
        for voyage in list_of_voyages:
            if voyage['Departure'][:10] == str(date):
                list_of_voyages_on_date.append(voyage)
        list_of_available_FAs = []
        list_of_unavailable_FAs = []
        for fa in list_of_FAs:
            for voyage in list_of_voyages_on_date:
                if voyage['FSM'] != fa['SSN'] and voyage['FA1'] != fa['SSN'] and voyage['FA2'] != fa['SSN']:
                    if fa not in list_of_available_FAs:
                        list_of_available_FAs.append(fa)
                else:
                    if fa not in list_of_unavailable_FAs:
                        list_of_unavailable_FAs.append(fa)
        if not list_of_voyages_on_date: # If no voyage on date -> all employees are available
            return list_of_FAs
        elif listType == "Available":
            return list_of_available_FAs
        elif listType == "Unavailable":
            return list_of_unavailable_FAs


    def getAvailabilityOfAll(self, date, listType):
        list_of_All = self.getEmployees()
        list_of_voyages = self.__ioAPI.loadVoyagesFromFile()
        list_of_voyages_on_date = []
        for voyage in list_of_voyages:
            if voyage['Departure'][:10] == str(date):
                list_of_voyages_on_date.append(voyage)
        list_of_available_All = []
        list_of_unavailable_All = []
        for emp in list_of_All:
            for voyage in list_of_voyages_on_date:
                if voyage['Captain'] != emp['SSN'] and voyage['Copilot'] != emp['SSN'] and voyage['FSM'] != emp['SSN']\
                     and voyage['FA1'] != emp['SSN'] and voyage['FA2'] != emp['SSN']:
                    if emp not in list_of_available_All:
                        list_of_available_All.append(emp)
                else:
                    if emp not in list_of_unavailable_All:
                        list_of_unavailable_All.append(emp)
                        list_of_unavailable_All.append([voyage['Destination']])
        if not list_of_voyages_on_date: # If no voyage on date -> all employees are available
            return list_of_All
        elif listType == "Available":
            return list_of_available_All
        elif listType == "Unavailable":
            return list_of_unavailable_All