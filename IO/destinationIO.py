from IO.BaseClassIO import BaseClassIO
from Model.destination import Destination
class DestinationIO (BaseClassIO):

    def __init__(self,filename):
        self.filename = filename
        self.temp_filename = 'IO/Data/temp_dest.csv'
    
    def loadDestinationFromFile(self):
        pass

    def storeDestinationToFile(self,dest):
        #country = Destination.
        dest_num = self.getDestID()
        country = Destination.get_country(dest)
        self.dest = Destination.get_destination(dest)
        airport = Destination.get_airport(dest)
        airtime = Destination.get_airtime(dest)
        dist = Destination.get_distance(dest)
        con_name = Destination.get_contact_name(dest)
        con_phone = Destination.get_contact_phone(dest)
        dest_id = self.get_destination_id()
        
        
        
        dest_info = '\n{},{},{},{},{},{},{},{},{}'.format(dest_id,self.dest,country,airport,airtime,dist,con_name,con_phone,dest_num)

        with open(self.filename,'a') as f:
            f.write(dest_info)


    def updateContactInfoInFile(self,line_index,row_index, updated_info):
        # Creates a temp_list so that we can use the indexes to change the correct information
        # Then we create a temp.csv file and later we use that temp file to overwrite 
        temp_list = []
        with open(self.filename,'r') as f:
            for line in f:
                line = line.split(',')
                temp_list.append(line)

        max_length = len(temp_list[0]) - 1
        # Needs to add \n if we are at the end of the line
        if row_index == max_length:
            temp_list[line_index][row_index] = updated_info + '\n'
        else:
            temp_list[line_index][row_index] = updated_info

        with open(self.temp_filename,'w+') as f:
            for line in temp_list:
                str_to_write = "{},{},{},{},{},{},{},{},{}".format(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
                f.write(str_to_write)
        
        with open(self.filename,'w') as f:
            for line in temp_list:
                str_to_write = "{},{},{},{},{},{},{},{},{}".format(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
                f.write(str_to_write)

                

    def get_destination_id(self):
        dest_id = self.dest[:3].upper()
        return dest_id