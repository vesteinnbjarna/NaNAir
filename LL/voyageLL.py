#from IO.IOAPI import IOAPI
import datetime

class VoyageLL ():

    def __init__(self, ioAPI_in):
        self.__ioAPI_in = ioAPI_in

    def createVoyage(self):
        pass

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
            departure_date = line['departure'][:10]
            if departure_date in week_list:
                list_of_voyages_week.append(line)

        return list_of_voyages_week

    def getVoyagesDay(self, date):
        list_of_voyages = self.__ioAPI_in.loadVoyagesFromFile()
        day_list = []
        for line in list_of_voyages:
            departure_date = line['departure'][:10]
            if departure_date == str(date):
                day_list.append(line)
        return day_list

    def updateVoyage(self):
        pass

