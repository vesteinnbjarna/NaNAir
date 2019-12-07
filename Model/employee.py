class Employee():
    def __init__(self, ssn, name, role, rank, address, phone_no, license):
        self.ssn = str(ssn)
        self.name = str(name)
        self.role = str(role)
        self.rank = str(rank)
        self.address = str(address)
        self.phone_no = str(phone_no)
        self.email = self.name.replace(" ",".").lower() + "@" + "nanair.is"
        self.id = 0

    def get_email(self):
        return self.email

    def assign_id(self, next_id):
        self.id = next_id
    
    def get_ssn(self):
        return self.ssn

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role

    def get_rank(self):
        return self.rank

    def get_address(self):
        return self.address

    def get_phonenumber(self):
        return self.phone_no
    
    def get_id(self):
        return self.id

#line[-1][0] = max_id 
#isol = Employee("0110972519", "Isol Sigurdardottir", "pilot", "captain", "Einiberg 21", "6613536", "tecnam")
#isol_email = isol.get_email()

#dilja = Employee("0203002050", "Dilja Sigurdardottir", "pilot", "co-pilot", "Einiberg 21", "6613136", "tecnam")
#dilja_email = dilja.get_email()
#rint(isol_email)
#print(dilja_email)
