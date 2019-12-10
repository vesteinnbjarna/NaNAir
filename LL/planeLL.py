#from IO.IOAPI import IOAPI
import datetime

class PlaneLL ():
    def __init__(self, ioAPI_in):
        self.__ioAPI_in = ioAPI_in

    def createPlane(self,plane):
        return self.__ioAPI_in.storePlaneToFile(plane)

    def getPlanes(self):
        return self.__ioAPI_in.loadPlanesFromFile()

    def getAvailablePlanes(self,date):
        planes = self.__ioAPI_in.loadPlanesFromFile()
        voyages = self.__ioAPI_in.loadVoyagesFromFile()
        availablePlanes_list = []
        today = date
        for line in planes:
            pass
    
