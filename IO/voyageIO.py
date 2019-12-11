from IO.BaseClassIO import BaseClassIO
from Model.voyage import Voyage
from Model.Destination import Destination

class VoyageIO (BaseClassIO):
   # def __init__(self,filename):
   #      self.voyageFileName = filename

    def loadVoyagesFromFile(self):
        pass

    def calculateArrival(self,voyage):
        departure = voyage.get_Departure()
        dest = voyage.get_dest()
        duration = dest.totalTime
        return departure + duration

    def storeVoyageToFile(self,voyage):
        voyageID = self.getNextID()
        flightNumber1 = voyage.get_FlightNumber1()
        flightNumber2 = voyage.get_FlightNumber2()
        dest = voyage.get_dest()
        destination_str = dest.destination
        departure = str(voyage.get_Departure()).replace(" ","T")
        arrival = str(self.calculateArrival(voyage)).replace(" ","T")
        aircraft = voyage.get_aircraft()
        aircraft_str = aircraft.registration
        captain = voyage.get_Captain()
        copilot = voyage.get_Copilot()
        fsm = voyage.get_FSM()
        fa1 = voyage.get_FA1()
        fa2 = voyage.get_FA2()

        voyage_str = '\n{},{},{},{},{},{},{},{},{},{},{},{}'.format(voyageID,flightNumber1,flightNumber2,destination_str,departure\
            ,arrival,aircraft_str,captain,copilot,fsm,fa1,fa2)

        with open(self.filename,'a') as f:
            f.write(voyage_str)

#id,fn1,fn2,destination,departure,arrival,aircraft,captain,copilot,fsm,fa1,fa2

    def updateVoyageInFile(self):
        pass