#from IO.IOAPI import IOAPI

class VoyageLL ():

    def __init__(self, ioAPI_in):
        self.__ioAPI_in = ioAPI_in

    def createVoyage(self):
        pass

    def getVoyages(self):
        return self.__ioAPI_in.loadVoyagesFromFile()


    def updateVoyage(self):
        pass

