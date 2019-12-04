class Destination():
    def __init__(self, country, airport, airtime, distance, contactName, contactPhone):
        self.country = country
        self.airport = airport
        self.airtime = airtime
        self.distance = distance
        self.contactName = contactName
        self.contactPhone = contactPhone

    
    def get_contact_info(self):
        return self.contactName, self.contactPhone
    
    def get_destination(self):
        return self.country, self.airport, self.airtime, self.distance



akureyri = Destination('Ísland', 'Akureyrarvöllur','00:45',383.0,'Gunnar Grímsson','5812345')
akureyri_CI = akureyri.get_contact_info()
akureyri_info = akureyri.get_destination()

print(akureyri_CI, akureyri_info)