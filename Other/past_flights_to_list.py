import csv 
import datetime
import dateutil.parser

def string_to_isoformat(flight_info_str):
        '''Parses the string to isoformat and gives filght_info_date the following attributes'''
        '''year, month, day, hour, minute, second'''

        flight_info_date = dateutil.parser.parse(flight_info_str)
        return (flight_info_date)


def print_flights_list(flights_list):
        '''prints past flights'''
        # Þarf að gera þessa lúppu því datetime library-ið er fáranlegt í prentun

        for row in flights_list:
                for i in range (len(row)):
                        if row[i] != row[-1]:
                                print(row[i], end=',')
                        else:
                                print(row[i])

def past_flights_to_list():
        with open('PastFlights.csv', mode = 'r') as csvfile:
                readCSV = csv.reader(csvfile, delimiter = ',')
                past_flights_list = []

                header = next(readCSV)
        
                for row in readCSV:
                
                        flight_num = row[0]
                        dep_fr = row[1]
                        arr_at =row[2]
                        departure = row[3]
                        arrival = row[4]
                        aircraft_id = row[5]
                        captain_ssn = row[6]
                        cop_ssn = row[7]
                        fsm_ssn = row[8]
                        fa1_ssn = row[9]
                        fa2_ssn = row[10]


                        dep_info = string_to_isoformat(departure)
                        arr_info = string_to_isoformat(arrival)
                        
                       
                        past_flights_list.append([flight_num,dep_fr,dep_info,arr_at,arr_info,aircraft_id,captain_ssn,cop_ssn,fsm_ssn,fa1_ssn,fa2_ssn])

                print_flights_list(past_flights_list)
                


flights_to_list()


