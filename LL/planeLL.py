#from IO.IOAPI import IOAPI
import datetime
from Model.Destination import Destination
from LL.voyageLL import VoyageLL
import collections

class PlaneLL ():
    def __init__(self, ioAPI_in):
        self.__ioAPI_in = ioAPI_in
        self.voyLL = VoyageLL(ioAPI_in)

    def createPlane(self,plane):
        return self.__ioAPI_in.storePlaneToFile(plane)

    def getPlanes(self):
        return self.__ioAPI_in.loadPlanesFromFile()

    def getPlaneType_list(self):
        return self.__ioAPI_in.loadPlaneTypesFromFile()

    def getPlaneType(self,registration):
        plane_list = self.__ioAPI_in.loadPlanesFromFile()
        for plane in plane_list:
            if plane['planeInsignia'] == registration:
                return plane['planeTypeId']

    def getAvailablePlanes(self,departureDateTime,totalTime):
        arrivalDateTime = departureDateTime + totalTime
        plane_list = self.getPlanes() # Starting with all planes available -> unavailable will be removed
        voyage_list = self.__ioAPI_in.loadVoyagesFromFile()
        available_planes_list = []
        voyages_on_same_time_list = []
        for voyage in voyage_list:
            voyage_departure = datetime.datetime.strptime(voyage['Departure'], '%Y-%m-%dT%H:%M:%S')
            voyage_arrival = datetime.datetime.strptime(voyage['Arrival'], '%Y-%m-%dT%H:%M:%S')
            if (departureDateTime <= voyage_departure <= arrivalDateTime)\
                or (departureDateTime <= voyage_arrival <= arrivalDateTime):
                voyages_on_same_time_list.append(voyage)
        unavailable_planes = []
        for voyage in voyages_on_same_time_list:
            unavailable_planes.append(voyage['Aircraft'])

        for plane in plane_list:
            if plane['planeInsignia'] not in unavailable_planes:
                available_planes_list.append(plane)

        return available_planes_list

    def getPlaneStatus(self,dateTime):
        planesWorking_list, planesNotWorking_list = self.getPlanesWorking(dateTime)
        working_odict = collections.OrderedDict()
        planesNotInAir = []
        allPlanes_status = []
        for plane in planesNotWorking_list:
            working_odict = collections.OrderedDict()
            working_odict['Aircraft ID'] = plane['planeInsignia']
            working_odict['Plane Type'] = plane['planeTypeId']
            working_odict['Current Flight Number'] = 'Not in flight'
            working_odict['Destination'] = 'N/A'
            planesNotInAir.append(working_odict)
        self.getPlaneInfo(planesNotInAir)
        planesInAir = self.getPlaneWorkingState(dateTime, planesWorking_list)
        for plane in planesInAir:
            allPlanes_status.append(plane)
        for plane in planesNotInAir:
            allPlanes_status.append(plane)
        return allPlanes_status

    def getPlaneWorkingState(self, dateTime, planesWorking_list):
        planesInAir = []
        working_odict = collections.OrderedDict()
        flightsOnDay = self.getFlightsOnDay(dateTime)
        for plane in planesWorking_list:
            for flight in flightsOnDay:
                flightDeparture = datetime.datetime.strptime(flight['departure'], "%Y-%m-%dT%H:%M:%S")
                flightArrival = datetime.datetime.strptime(flight['arrival'], "%Y-%m-%dT%H:%M:%S")
                if flight['aircraftID'] == plane['planeInsignia'] and \
                    flightDeparture <= dateTime <= flightArrival:
                    working_odict = collections.OrderedDict()
                    working_odict['Aircraft ID'] = plane['planeInsignia']
                    working_odict['Plane Type'] = plane['planeTypeId']
                    working_odict['Current Flight Number'] = flight['flightNumber']
                    working_odict['Destination'] = flight['arrivingAt']
                    planesInAir.append(working_odict)
        self.getPlaneInfo(planesInAir)
        return planesInAir

    def getPlaneInfo(self, planesInAir):
        planeTypes = self.__ioAPI_in.loadPlaneTypesFromFile()
        for plane in planesInAir:
            for planeType in planeTypes:
                if plane['Plane Type'] == planeType['planeTypeId']:
                    plane['Seats'] = planeType['capacity']

    def getFlightsOnDay(self, dateTime):
        allFlights = self.__ioAPI_in.loadRoutesFromFile()
        flightsOnDay = []
        for flight in allFlights:
            if flight['departure'][:10] == str(dateTime.date()):
                flightsOnDay.append(flight)
        return flightsOnDay

    def getPlanesWorking(self, dateTime):
        self.voyageOnDay_list = self.voyLL.getVoyagesDay(dateTime)
        plane_list = self.__ioAPI_in.loadPlanesFromFile()
        planesNotWorking_list = []
        planesWorking_list = []
        for plane in plane_list:
            for voyage in self.voyageOnDay_list:
                voy_departure = datetime.datetime.strptime(voyage['Departure'], "%Y-%m-%dT%H:%M:%S")
                voy_arrival = datetime.datetime.strptime(voyage['Arrival'], "%Y-%m-%dT%H:%M:%S")
                if plane['planeInsignia'] == voyage['Aircraft'] and voy_departure <= dateTime <= voy_arrival:
                    planesWorking_list.append(plane)
                else:
                    planesNotWorking_list.append(plane)
        return planesWorking_list, planesNotWorking_list



 
