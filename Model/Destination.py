class Destination():
    def __init__(self, destination, country, airport, airtime, distance, contactName, contactPhone):
        self.destination = destination
        self.country = country
        self.airport = airport
        self.airtime = airtime
        self.distance = distance
        self.contactName = contactName
        self.contactPhone = contactPhone

    
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



#akureyri = Destination('Ísland', 'Akureyrarvöllur','00:45',383.0,'Gunnar Grímsson','5812345')
#akureyri_CI = akureyri.get_contact_info()
#akureyri_info = akureyri.get_destination()

#print(akureyri_CI, akureyri_info)