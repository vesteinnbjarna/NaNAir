from IO.BaseClassIO import BaseClassIO
class RouteIO (BaseClassIO):

    def storeRouteOutToFile(self,route):
        routeID = self.getNextID()
        flightNumber = route.getFlightNumber()
        departingFrom = route.getDepartingFrom()
        arrivingAt_obj = route.getArrivingAt()
        arrivingAt_str = arrivingAt_obj.get_destination()[:3].upper()
        departure = str(route.getDeparture()).replace(' ','T')
        arrival = str(route.getArrival()).replace(' ','T')
        aircraft_obj = route.getAircraft()
        aircraftID = aircraft_obj.get_registration()
        captain = route.getCaptain()
        copilot = route.getCopilot()
        fsm = route.getFSM()
        fa1 = route.getFA1()
        fa2 = route.getFA2()

        routeOut_str = '\n{},{},{},{},{},{},{},{},{},{},{},{}'.format(routeID,flightNumber,\
            departingFrom,arrivingAt_str,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2)
        with open(self.filename,'a') as f:
            f.write(routeOut_str)

    def storeRouteInToFile(self,route):
        routeID = self.getNextID()
        flightNumber = route.getFlightNumber()
        departingFrom_obj = route.getDepartingFrom()
        departingFrom_str = departingFrom_obj.get_destination()[:3].upper()
        arrivingAt = route.getArrivingAt()
        departure = str(route.getDeparture()).replace(' ','T')
        arrival = str(route.getArrival()).replace(' ','T')
        aircraft_obj = route.getAircraft()
        aircraftID = aircraft_obj.get_registration()
        captain = route.getCaptain()
        copilot = route.getCopilot()
        fsm = route.getFSM()
        fa1 = route.getFA1()
        fa2 = route.getFA2()

        routeIn_str = '\n{},{},{},{},{},{},{},{},{},{},{},{}'.format(routeID,flightNumber,\
            departingFrom_str,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2)
        with open(self.filename,'a') as f:
            f.write(routeIn_str)


