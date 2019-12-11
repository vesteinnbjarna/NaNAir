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
            if voyage['departure'][:10] == str(date):
                list_of_voyages_on_date.append(voyage)
        list_of_available_pilots = []
        list_of_unavailable_pilots = []
        for pilot in list_of_pilots:
            for voyage in list_of_voyages_on_date:
                if voyage['captain'] != pilot['SSN'] and voyage['copilot'] != pilot['SSN']:
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
            if voyage['departure'][:10] == str(date):
                list_of_voyages_on_date.append(voyage)
        list_of_available_FAs = []
        list_of_unavailable_FAs = []
        for fa in list_of_FAs:
            for voyage in list_of_voyages_on_date:
                if voyage['fsm'] != fa['SSN'] and voyage['fa1'] != fa['SSN'] and voyage['fa2'] != fa['SSN']:
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
            if voyage['departure'][:10] == str(date):
                list_of_voyages_on_date.append(voyage)
        list_of_available_All = []
        list_of_unavailable_All = []
        for emp in list_of_All:
            for voyage in list_of_voyages_on_date:
                if voyage['captain'] != emp['SSN'] and voyage['copilot'] != emp['SSN'] and voyage['fsm'] != emp['SSN']\
                     and voyage['fa1'] != emp['SSN'] and voyage['fa2'] != emp['SSN']:
                    if emp not in list_of_available_All:
                        list_of_available_All.append(emp)
                else:
                    if emp not in list_of_unavailable_All:
                        list_of_unavailable_All.append(emp)
                        list_of_unavailable_All.append([voyage['arrivingAt']])
        if not list_of_voyages_on_date: # If no voyage on date -> all employees are available
            return list_of_All
        elif listType == "Available":
            return list_of_available_All
        elif listType == "Unavailable":
            return list_of_unavailable_All