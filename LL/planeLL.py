#from IO.IOAPI import IOAPI
import datetime
from Model.Destination import Destination
from LL.voyageLL import VoyageLL

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


    def getPlaneStatus(self, chosenPlane, date, time):
        voyageOnDay_list = self.voyLL.getVoyagesDay(date)
        plane_list = self.__ioAPI_in.loadPlanesFromFile()
        planesNotWorking_list = []
        planesWorking_list = []
        for plane in plane_list:
            for voyage in voyageOnDay_list:
                if plane['planeInsignia'] == voyage['Aircraft']:
                    planesWorking_list.append(plane)
                else:
                    planesNotWorking_list.append(plane)

        return voyage_list



 
