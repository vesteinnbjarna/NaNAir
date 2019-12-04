import csv 

with open('Crew.csv', mode = 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    ssn = []
    employee_list = []

    header = next(readCSV)
    
    for row in readCSV:
        ssn = row[0]
        emp_name = row[1]
        emp_role = row[2]
        emp_rank = row[3]
        emp_licence = row[4]
        emp_address = row[5]
        emp_phoneno = row[6]
        #emp_email = row[7]

        employee_list.append([ssn, emp_name, emp_role, emp_role, emp_licence, emp_address, emp_phoneno])

    
    for row in employee_list:
        ssn = row[0]
        emp_name = row[1]
        emp_role = row[2]
        emp_rank = row[3]
        emp_licence = row[4]
        emp_address = row[5]
        emp_phoneno = row[6]
        #emp_email = row[7]
        
        print( 'Name: {}, Role: {}, Rank: {}, License: {}, Address: {}, Phone: {}'.format(emp_name, emp_role, emp_rank,emp_licence,emp_address, emp_phoneno))

        