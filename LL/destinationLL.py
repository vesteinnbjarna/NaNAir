#from IO.IOAPI import IOAPI
from Model.Destination import Destination

class DestinationLL ():
    def __init__(self, ioAPI_in):
        self.__ioAPI = ioAPI_in
        
    def storeDestinationToFile(self,dest):
        self.__ioAPI.storeDestinationToFile(dest)

    def getDestination(self):
        return self.__ioAPI.loadDestinationFromFile()

    def updateContactInfo(self, line_index,row_index, updated_info):
        self.__ioAPI.updateContactInfoInFile(line_index,row_index, updated_info)
    
    def getDestinationHeader(self,list_of_destination):
        header_list = []
        counter = 0
        while counter < 1:
            for line in list_of_destination:
                for k,v in line.items():
                    header_list.append(k)
                counter += 1
                break


        return header_list


    def getDestinationValue(self,list_of_destination):
        value_list = []
        for line in list_of_destination:
                d_id = line["ID"]
                d_dest = line["Destination"]
                d_country = line["Country"]
                d_airp = line["Airport"]
                d_airt = line["Airtime"]
                d_dist = line["Distance"]
                d_con_name = line["Contact name"]
                d_con_phone_number = line["Contact phone"]
                d_dest_number = line["Destination number"]
                value_list.append([d_id,d_dest,d_country,d_airp,d_airt,d_dist,d_con_name,d_con_phone_number,d_dest_number])
                
        return value_list
       

    def getDestinationsContactInfo(self):
        '''returns a list with destination'''
        '''and contact information'''
        temp_list = self.__ioAPI.loadDestinationFromFile()
        dest_list = []
        for line in temp_list:
            for k,v in line.items():
                if k == 'Destination':
                    dest = v
                elif k == 'Contact name':
                    con_name = v
                
                elif k == 'Contact phone':
                    con_phone = v

            dest_list.append([dest,con_name,con_phone])
        
        return dest_list  

    def createDestinationObject(self,destination_str):
        dest_list = self.__ioAPI.loadDestinationFromFile()
        dest_odict = {}
        for dest in dest_list:
            if dest['Destination'] == destination_str:
                dest_odict = dest
        destination_obj = Destination(dest_odict['Destination'],dest_odict['Country'],dest_odict['Airport'],\
            dest_odict['Airtime'],dest_odict['Distance'],dest_odict['Contact name'],dest_odict['Contact phone'])
        return destination_obj


#destination, country, airport, airtime, distance, contactName, contactPhone):
    