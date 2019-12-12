#from IO.IOAPI import IOAPI
import datetime

class VoyageLL ():

    def __init__(self, ioAPI_in):
        self.__ioAPI_in = ioAPI_in

    def createVoyage(self,voyage):
        return self.__ioAPI_in.storeVoyageToFile(voyage)

    def getVoyages(self):
        return self.__ioAPI_in.loadVoyagesFromFile()

    def getVoyagesWeek(self, first_day_of_week):
        list_of_voyages = self.__ioAPI_in.loadVoyagesFromFile()
        list_of_voyages_week = []
        week_list = [str(first_day_of_week)]
        tdelta = datetime.timedelta(days=1)
        nextDay = first_day_of_week + tdelta
        for counter in range(6):
            week_list.append(str(nextDay))
            nextDay += tdelta
        for line in list_of_voyages:
            departure_date = line['Departure'][:10]
            if departure_date in week_list:
                list_of_voyages_week.append(line)

        return list_of_voyages_week

    def getVoyagesDay(self, date):
        list_of_voyages = self.__ioAPI_in.loadVoyagesFromFile()
        day_list = []
        for line in list_of_voyages:
            departure_date = line['Departure'][:10]
            if departure_date == str(date):
                day_list.append(line)
        return day_list 

    def updateVoyage(self):
        pass

    def getVoyageHeader(self, voyage_list):
        header_list = []
        counter = 0
        for line in voyage_list:
            if counter < 1:
                for k,v in line.items():
                    header_list.append(k)
                counter += 1
                return header_list

    def getVoyageValue(self,voyage_list):
        value_list = []
        try:
            for line in voyage_list:
                v_id = line["ID"]
                v_fn1 = line["FN1"]
                v_fn2 = line["FN2"]
                v_dest = line["Destination"]
                v_depart = line["Departure"]
                v_arr = line["Arrival"]
                v_airc = line["Aircraft"]
                v_capt = line["Captain"]
                v_cop = line["Copilot"]
                v_fsm = line["FSM"]
                v_fa1 = line["FA1"]
                v_fa2 = line["FA2"]
                value_list.append(
                    [v_id,v_fn1,v_fn2,v_dest,v_depart,v_arr,v_airc,v_capt,v_cop,v_fsm,v_fa1,v_fa2])
            return value_list
        except TypeError:
            return None

    def getUnmannedVoyages(self):
        voyages_list = self.__ioAPI_in.loadVoyagesFromFile()
        unmannedVoyages_list = []
        for voyage in voyages_list:
            if not voyage['Captain']:
                unmannedVoyages_list.append(voyage)
        unmannedVoyagesValues_list = self.getVoyageValue(unmannedVoyages_list)
        unmannedVoyagesHeaders_list = self.getVoyageHeader(unmannedVoyages_list)
        return unmannedVoyagesValues_list, unmannedVoyagesHeaders_list


    def storeCrewToFile(self,voyage):
        self.__ioAPI_in.storeCrewToFile(voyage)