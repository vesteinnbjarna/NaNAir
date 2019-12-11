import csv

class BaseClassIO ():

    def __init__(self, filename):
        self.filename = filename

    def loadFile(self):
        working_list = []
        with open(self.filename, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for line in csv_reader:
                working_list.append(line)
        return working_list

    def getNextID(self):
        maxList = []
        with open (self.filename, 'r') as f:
            for line in f:
                maxList.append(line.split(','))
        
        self.maxId = int(maxList[-1][0]) + 1
        return self.maxId 

    def getDestID (self):
        maxList = []
        with open (self.filename, 'r') as f:
            for line in f:
                maxList.append(line.split(','))
        
        self.destID = int(maxList[-1][-1]) + 1
        self.destID = str(self.destID)
        if len(self.destID) == 1:
            self.destID = "0"+self.destID
        return self.destID 
            
    

    
            
    