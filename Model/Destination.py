import datetime

class Destination():
    def __init__(self, destination, country, airport, airtime, distance, contactName, contactPhone):
        self.destination = destination
        self.country = country
        self.airport = airport
        self.airtime = airtime
        self.distance = distance
        self.contactName = contactName
        self.contactPhone = contactPhone
        self.totalTime = self.calculate_total_time()
    
    def calculate_total_time(self):
        hours = self.airtime[:2]
        if hours[0] == '0':
            hours_int = int(hours[1:])
        else:
            hours_int = int(hours)
        minutes = self.airtime[3:]
        if minutes[0] == '0':
            minutes_int = int(minutes[1:])
        else:
            minutes_int = int(minutes)

        tdelta_oneHour = datetime.timedelta(hours=1)
        tdelta_leg = datetime.timedelta(hours=hours_int, minutes=minutes_int)

        totalTime = tdelta_leg + tdelta_oneHour + tdelta_leg
        return totalTime

    def get_destination(self):
        return self.destination

    def get_country(self):
        return self.country
    
    def get_airport(self):
        return self.airport

    def get_airtime(self):
        return self.airtime

    def get_distance(self):
        return self.distance

    def get_contact_name (self):
        return self.contactName
    
    def get_contact_phone (self):
        return self.contactPhone



# akureyri = Destination('Reykjavik','Iceland','Reykjarvíkurflugvöllur','03:14','1000','isol','6613536')
# print(akureyri.calculate_total_time())
# #akureyri_CI = akureyri.get_contact_info()
# akureyri_info = akureyri.get_destination()

# #print(akureyri_CI, akureyri_info)