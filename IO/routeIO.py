from IO.BaseClassIO import BaseClassIO
import datetime
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

        routeOut_str = '\n{},{},{},{},{},{},{}'.format(routeID,flightNumber,\
            departingFrom,arrivingAt_str,departure,arrival,aircraftID)
        with open(self.filename,'a') as f:
            f.write(routeOut_str)

    def storeRouteInToFile(self,route):
        self.routeID = self.getNextID()
        flightNumber = route.getFlightNumber()
        departingFrom_obj = route.getDepartingFrom()
        departingFrom_str = departingFrom_obj.get_destination()[:3].upper()
        arrivingAt = route.getArrivingAt()
        departure = str(route.getDeparture()).replace(' ','T')
        arrival = str(route.getArrival()).replace(' ','T')
        aircraft_obj = route.getAircraft()
        aircraftID = aircraft_obj.get_registration() 
    

        routeIn_str = '\n{},{},{},{},{},{},{}'.format(self.routeID,flightNumber,\
            departingFrom_str,arrivingAt,departure,arrival,aircraftID)
        with open(self.filename,'a') as f:
            f.write(routeIn_str)
