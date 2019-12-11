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

    def getAvailablePlanes(self,date,totalTime):
        plane_list = self.getPlanes()
        voyage_list = self.__ioAPI_in.loadVoyagesFromFile()
        voyages_on_same_time_list = []
        for voyage in voyage_list:
            pass

        for plane in plane_list:
            for voyage in voyage_list:
                pass

 