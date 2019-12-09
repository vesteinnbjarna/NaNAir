from IO.BaseClassIO import BaseClassIO
from Model.employee import Employee

class EmployeeIO (BaseClassIO):
    def __init__(self,filename):
       self.filename = filename
       self.temp_filename = 'IO/Data/temp_emp.csv'
    
    #def loadEmployeesFromFile(self):
    #    pass

    def storeEmployeeToFile(self,employee):
        next_id = self.getNextID()
        #Employee.assign_id(next_id)

        ssn = Employee.get_ssn(employee)
        name = Employee.get_name(employee)
        role = Employee.get_role(employee)
        #rank = Employee.get_rank(employee)
        address = Employee.get_address(employee)
        phone_no = Employee.get_phonenumber(employee)
        email = Employee.get_email(employee)
        emp_id = next_id   #str(Employee.get_id(employee))
        emp_license = Employee.get_license(employee)

        employee_info = '\n{},{},{},{},{},{},{},{}'.format(emp_id,ssn,name,role,emp_license,address,phone_no,email)
        print(employee_info)
        
        
        with open(self.filename,'a') as f:
            f.write(employee_info)
        



    def updateEmployeeInFile(self, line_index, row_index, updated_info):
        line_index = int(line_index)
        temp_list = []
        with open(self.filename,'r') as f:
            for line in f:
                line = line.split(',')
                temp_list.append(line)
        max_length = len(temp_list[0])-1
        if row_index == max_length:
            temp_list[line_index][row_index] = updated_info + '\n'
        else:
            temp_list[line_index][row_index] = updated_info

        with open(self.temp_filename,'w+') as f:
            for line in temp_list:
                emp_id = line[0]
                emp_ssn = line[1]
                emp_name = line[2]
                emp_role = line[3]
                emp_rank = line[4]
                emp_licence = line[5]
                emp_address = line[6]
                emp_pho_no = line[7]
                emp_email = line[8]
                str_to_write = '{},{},{},{},{},{},{},{},{}'.format(emp_id,emp_ssn,emp_name,emp_role,emp_rank,emp_licence,emp_address,emp_pho_no,emp_email)
                f.write(str_to_write)
                

        with open(self.filename,'w') as f:
            for line in temp_list:
                emp_id = line[0]
                emp_ssn = line[1]
                emp_name = line[2]
                emp_role = line[3]
                emp_rank = line[4]
                emp_licence = line[5]
                emp_address = line[6]
                emp_pho_no = line[7]
                emp_email = line[8]
                str_to_write = '{},{},{},{},{},{},{},{},{}'.format(emp_id,emp_ssn,emp_name,emp_role,emp_rank,emp_licence,emp_address,emp_pho_no,emp_email)
                f.write(str_to_write)