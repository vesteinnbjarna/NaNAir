from IO.BaseClassIO import BaseClassIO
from Model.destination import Destination
class DestinationIO (BaseClassIO):
    
    def loadDestinationFromFile(self):
        pass

    def storeDestinationToFile(self,dest):
        #country = Destination.
        country = Destination.get_country(dest)
        self.dest = Destination.get_destination(dest)
        airport = Destination.get_airport(dest)
        airtime = Destination.get_airtime(dest)
        dist = Destination.get_distance(dest)
        con_name = Destination.get_contact_name(dest)
        con_phone = Destination.get_contact_phone(dest)
        dest_id = self.get_destination_id()
        
        
        
        dest_info = '\n{},{},{},{},{},{},{},{}'.format(dest_id,self.dest,country,airport,airtime,dist,con_name,con_phone)

        with open(self.filename,'a') as f:
            f.write(dest_info)


    def updateContactInfoInFile(self):
        pass

    def get_destination_id(self):
        dest_id = self.dest[:3].upper()
        return dest_id