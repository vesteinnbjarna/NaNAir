#from IO.IOAPI import IOAPI

class DestinationLL ():
    def __init__(self, ioAPI_in):
        self.__ioAPI = ioAPI_in
        
    def storeDestinationToFile(self,dest):
        self.__ioAPI.storeDestinationToFile(dest)

    def getDestination(self):
        return self.__ioAPI.loadDestinationFromFile()

    def updateContactInfo(self, line_index,row_index, updated_info):
        self.__ioAPI.updateContactInfoInFile(line_index,row_index, updated_info)
    
    def getDestinationsContactInfo(self):
        '''returns a list with destination'''
        '''and contact information'''
        temp_list = self.__ioAPI.loadDestinationFromFile()
        dest_list = []
        for line in temp_list:
            for k,v in line.items():
                if k == 'destination':
                    dest = v
                elif k == 'contact name':
                    con_name = v
                
                elif k == 'contact phone':
                    con_phone = v

            dest_list.append([dest,con_name,con_phone])
        
        return dest_list  

    