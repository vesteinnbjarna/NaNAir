from Model.Destination import Destination
from Model.employee import Employee
from Model.plane import Plane
from Model.route import Route
import datetime

class Voyage(Destination): 

    def __init__(self, destination, aircraft, departure, voyageID = 0):
        self.destination = destination
        self.aircraft = aircraft
        self.flightNumber1 = 0
        self.flightNumber2 = 0
        self.departure = departure
        self.captain = ''
        self.copilot = ''
        self.fsm = ''
        self.fa1 = ''
        self.fa2 = ''
        self.voyageID = voyageID
        self.airtime = datetime.datetime.strptime(self.destination.get_airtime(), '%H:%M').time()
        self.routeOutArrival = self.calculateRouteOutArrival()
        self.routeInDeparture = self.calculateRouteInDeparture()
        self.arrival = self.calculateArrival()
        self.routeOut = Route(self.flightNumber1,'Reykjavík',self.destination,self.departure,self.routeOutArrival,self.aircraft)
        self.routeIn = Route(self.flightNumber2,self.destination,'Reykjavík,',self.routeInDeparture,self.arrival,self.aircraft)

    def calculateRouteOutArrival(self):
        self.tdelta_airtime = datetime.timedelta(hours=self.airtime.hour,minutes=self.airtime.minute)
        routeOutArrival = self.departure + self.tdelta_airtime
        return routeOutArrival

    def calculateRouteInDeparture(self):
        self.tdelta_OneHour = datetime.timedelta(hours=1)
        routeInDeparture = self.departure + self.tdelta_airtime + self.tdelta_OneHour
        return routeInDeparture
    
    def calculateArrival(self):
        arrival = self.departure + 2 * self.tdelta_airtime + self.tdelta_OneHour
        return arrival

    def assignCaptain(self, captain):
        self.routeOut.assignCaptain(captain)
        self.routeIn.assignCaptain(captain)
        self.captain = captain

    def assignCopilot(self, copilot):
        self.routeOut.assignCopilot(copilot)
        self.routeIn.assignCopilot(copilot)
        self.copilot = copilot

    def assingFSM(self, fsm):
        self.routeOut.assignFSM(fsm)
        self.routeIn.assignFSM(fsm)
        self.fsm = fsm

    def assignFA1(self, fa1):
        self.routeOut.assignFA1(fa1)
        self.routeIn.assignFA1(fa1)
        self.fa1 = fa1

    def assignFA2(self, fa2):
        self.routeOut.assignFA2(fa2)
        self.routeIn.assignFA2(fa2)
        self.fa2 = fa2

    def assingFlightNumber1(self,flightnumber):
        self.routeOut.assignFlightNumber(flightnumber)
        self.flightNumber1 = flightnumber

    def assingFlightNumber2(self,flightnumber):
        self.routeIn.assignFlightNumber(flightnumber)
        self.flightNumber2 = flightnumber

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

    def get_ID(self):
        return self.voyageID