class Employee():
    def __init__(self, ssn, name, role, rank, address, phone_no, license):
        self.ssn = ssn
        self.name = name
        self.role = role
        self.rank = rank
        self.address = address
        self.phone_no = phone_no
        self.email = self.name.replace(" ",".").lower() + "@" + "nanair.is"
    
    def get_email(self):
        return self.email

#isol = Employee("0110972519", "Isol Sigurdardottir", "pilot", "captain", "Einiberg 21", "6613536", "tecnam")
#isol_email = isol.get_email()

#dilja = Employee("0203002050", "Dilja Sigurdardottir", "pilot", "co-pilot", "Einiberg 21", "6613136", "tecnam")
#dilja_email = dilja.get_email()
#rint(isol_email)
#print(dilja_email)
