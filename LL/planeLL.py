#from IO.IOAPI import IOAPI
import datetime
from Model.Destination import Destination

class PlaneLL ():
    def __init__(self, ioAPI_in):
        self.__ioAPI_in = ioAPI_in

    def createPlane(self,plane):
        return self.__ioAPI_in.storePlaneToFile(plane)

    def getPlanes(self):
        return self.__ioAPI_in.loadPlanesFromFile()

    def getAvailablePlanes(self,departureDateTime,totalTime):
        arrivalDateTime = departureDateTime + totalTime
        plane_list = self.getPlanes() # Starting with all planes available -> unavailable will be removed
        voyage_list = self.__ioAPI_in.loadVoyagesFromFile()
        available_planes_list = []
        voyages_on_same_time_list = []
        for voyage in voyage_list:
            voyage_departure = datetime.datetime.strptime(voyage['departure'], '%Y-%m-%dT%H:%M:%S')
            voyage_arrival = datetime.datetime.strptime(voyage['arrival'], '%Y-%m-%dT%H:%M:%S')
            if (departureDateTime <= voyage_departure <= arrivalDateTime)\
                or (departureDateTime <= voyage_arrival <= arrivalDateTime):
                voyages_on_same_time_list.append(voyage)
        unavailable_planes = []
        for voyage in voyages_on_same_time_list:
            unavailable_planes.append(voyage['aircraft'])

        for plane in plane_list:
            if plane['planeInsignia'] not in unavailable_planes:
                available_planes_list.append(plane)

        return available_planes_list
 