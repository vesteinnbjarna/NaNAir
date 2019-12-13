import datetime

class VoyageLL ():

    def __init__(self, ioAPI_in):
        self.__ioAPI_in = ioAPI_in

    def createVoyage(self,voyage):
        flightNumber1, flightNumber2 = self.getFlightNumbers(voyage)
        voyage.assingFlightNumber1(flightNumber1)
        voyage.assingFlightNumber2(flightNumber2)
        return self.__ioAPI_in.storeVoyageToFile(voyage)

    def getVoyages(self):
        dateTimeNow = datetime.datetime.now()
        allVoyages = self.__ioAPI_in.loadVoyagesFromFile()
        for voyage in allVoyages:
            voyageDeparture = datetime.datetime.strptime(voyage['Departure'], '%Y-%m-%dT%H:%M:%S')
            voyageArrival = datetime.datetime.strptime(voyage['Arrival'], '%Y-%m-%dT%H:%M:%S')
            if dateTimeNow < voyageDeparture:
                voyage['Status'] = 'Not started'
            elif dateTimeNow > voyageArrival:
                voyage['Status'] = 'Complete'
            else:
                voyage['Status'] = 'In progress'

        return allVoyages #self.__ioAPI_in.loadVoyagesFromFile()

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
            if departure_date == str(date.date()):
                day_list.append(line)
        return day_list 

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
                if len(line) == 13:
                    v_stat = line['Status']
                    value_list.append(
                        [v_id,v_fn1,v_fn2,v_dest,v_depart,v_arr,v_airc,v_capt,v_cop,v_fsm,v_fa1,v_fa2,v_stat])
                else:
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

    def getFullyStaffedVoyages(self):
        voyages_list = self.__ioAPI_in.loadVoyagesFromFile()
        mannedVoyages_list = []
        for voyage in voyages_list:
            if voyage['Captain']:
                mannedVoyages_list.append(voyage)
        mannedVoyagesValues_list = self.getVoyageValue(mannedVoyages_list)
        mannedVoyagesHeaders_list = self.getVoyageHeader(mannedVoyages_list)
        return mannedVoyagesValues_list, mannedVoyagesHeaders_list

    def getFlightNumbers(self,voyage):
        destNumber_str = self.getDestinationNumber(voyage)
        voyages_sameDestSameDay_int = self.getVoy_SameDaySameDest(voyage)
        flightNumber1 = 'NA' + destNumber_str + str(voyages_sameDestSameDay_int * 2)
        flightNumber2 = 'NA' + flightNumber1[2:4] + str(int(flightNumber1[4]) + 1)
        return flightNumber1, flightNumber2

    def getVoy_SameDaySameDest(self,voyage):
        voyages_list = self.__ioAPI_in.loadVoyagesFromFile()
        voyagesOnSameDay_int = 0
        for a_voyage in voyages_list:
            a_voyageDepartureDate = a_voyage['Departure'][:10]
            voyageDepartureDate = str(voyage.get_Departure())[:10]
            voyage_dest_obj = voyage.get_dest()
            voyage_dest_str = voyage_dest_obj.destination
            if a_voyageDepartureDate == voyageDepartureDate and a_voyage['Destination'] == voyage_dest_str:
                voyagesOnSameDay_int += 1
        return voyagesOnSameDay_int

    def getDestinationNumber(self,voyage):
        destination_list = self.__ioAPI_in.loadDestinationFromFile()
        voyageDestination_obj = voyage.get_dest()
        destination_str = voyageDestination_obj.destination
        for destination in destination_list:
            if destination['Destination'] == destination_str:
                return destination['Destination number']

    def storeCrewToFile(self,voyage):
        self.__ioAPI_in.storeCrewToFile(voyage)
