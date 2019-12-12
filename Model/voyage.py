from Model.Destination import Destination
from Model.employee import Employee
from Model.plane import Plane

class Voyage(Destination): 

    def __init__(self, destination, aircraft, departure, voyageID = 0):
        self.destination = destination
        self.aircraft = aircraft
        self.flightNumber1 = 1
        self.flightNumber2 = 1
        self.departure = departure
        self.captain = ''
        self.copilot = ''
        self.fsm = ''
        self.fa1 = ''
        self.fa2 = ''
        self.voyageID = voyageID

    def assignCaptain(self, captain):
        self.captain = captain

    def assignCopilot(self, copilot):
        self.copilot = copilot

    def assingFSM(self, fsm):
        self.fsm = fsm

    def assignFA1(self, fa1):
        self.fa1 = fa1

    def assignFA2(self, fa2):
        self.fa2 = fa2

    def get_dest(self):
        #return Destination.get_destination(self.destination)
        return self.destination
    
    def get_aircraft(self):
        return self.aircraft
    
    def get_FlightNumber1(self):
        return self.flightNumber1
    
    def get_FlightNumber2(self):
        return self.flightNumber2

    def get_Departure(self):
        return self.departure
    
    def get_Captain(self):
        return self.captain
    
    def get_Copilot(self):
        return self.copilot

    def get_FSM(self):
        return self.fsm

    def get_FA1(self):
        return self.fa1
    
    def get_FA2(self):
        return self.fa2

    def calculateFlightNumber(self):
        pass

    def get_ID(self):
        return self.voyageID