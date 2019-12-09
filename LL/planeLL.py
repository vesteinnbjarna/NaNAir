#from IO.IOAPI import IOAPI
class PlaneLL ():
    def __init__(self, ioAPI_in):
        self.__ioAPI_in = ioAPI_in

    def createPlane(self,plane):
        return self.__ioAPI_in.storePlaneToFile(plane)

    def getPlanes(self):
        return self.__ioAPI_in.loadPlanesFromFile()

