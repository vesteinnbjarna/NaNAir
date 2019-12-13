from IO.BaseClassIO import BaseClassIO
from Model.voyage import Voyage
from Model.Destination import Destination

class VoyageIO (BaseClassIO):

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
        fa2 = voyage.get_FA2() + "\n"

        voyage_str = "{},{},{},{},{},{},{},{},{},{},{},{}".format(voyageID,flightNumber1,flightNumber2,destination_str,departure\
            ,arrival,aircraft_str,captain,copilot,fsm,fa1,fa2)

        with open(self.filename,'a') as f:
            f.write(voyage_str)

    def storeCrewToFile(self,voyage):
        
        line_index = int(Voyage.get_ID(voyage))
        capt = Voyage.get_Captain(voyage)
        cop = Voyage.get_Copilot(voyage)
        fsm = Voyage.get_FSM(voyage)
        fa1 = Voyage.get_FA1(voyage)
        fa2 = Voyage.get_FA2(voyage)

        with open(self.filename,'r') as f:
            temp_list = []
            for line in f:
                line = line.split(',')
                temp_list.append(line)

        temp_list[line_index][7] = capt
        temp_list[line_index][8] = cop
        temp_list[line_index][9] = fsm
        temp_list[line_index][10] = fa1
        temp_list[line_index][11] = fa2 + "\n"

        with open("IO/Data/temp_voyage.csv",'w+') as f:
            for line in temp_list:
                voy_to_write = "{},{},{},{},{},{},{},{},{},{},{},{}".format(line[0],line[1],line[2],line[3],
                line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11])
                
                f.write(voy_to_write)

        with open(self.filename,'w') as f:
            for line in temp_list:
                voy_to_write = "{},{},{},{},{},{},{},{},{},{},{},{}".format(line[0],line[1],line[2],line[3],
                line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11])
                
                f.write(voy_to_write)


        
        

