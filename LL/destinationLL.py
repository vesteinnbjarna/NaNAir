#from IO.IOAPI import IOAPI

class DestinationLL ():
    def __init__(self, ioAPI_in):
        self.__ioAPI = ioAPI_in
        
    def storeDestinationToFile(self,dest):
        self.__ioAPI.storeDestinationToFile(dest)

    def getDestination(self):
        self.__ioAPI.loadDestinationFromFile()
    

    def updateContactInfo(self):
        self.__ioAPI.updateContactInfoInFile()
        

    