class Route():
    def __init__(self,flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftID,captain = '',copilot = '',fsm = '',fa1 = '',fa2 = ''):
        self.flightNumber = flightNumber
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt
        self.departure = departure
        self.arrival = arrival
        self.aircraftID = aircraftID
        self.captain = captain
        self.copilot = copilot
        self.fsm = fsm
        self.fa1 = fa1
        self.fa2 = fa2

    def assignCaptain(self,captain):
        self.captain = captain

    def assignCopilot(self,copilot):
        self.copilot = copilot

    def assignFSM(self,fsm):
        self.fsm = fsm

    def assignFA1(self,fa1):
        self.fa1 = fa1

    def assignFA2(self,fa2):
        self.fa2 = fa2

    def getFlightNumber(self):
        return self.flightNumber

    def getDepartingFrom(self):
        return self.departingFrom

    def getArrivingAt(self):
        return self.arrivingAt

    def getDeparture(self):
        return self.departure

    def getArrival(self):
        return self.arrival

    def getAircraftID(self):
        return self.aircraftID
    
    def getCaptain(self):
        return self.captain
    
    def getCopilot(self):
        return self.copilot

    def getFSM(self):
        return self.fsm

    def getFA1(self):
        return self.fa1

    def getFA2(self):
        return self.fa2

#id,flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2