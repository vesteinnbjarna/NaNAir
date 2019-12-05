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

    

    
            
    