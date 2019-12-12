class Plane():
    def __init__(self,registration,planeType):
        self.registration = registration
        self.planeType = planeType

    def get_registration(self):
        return self.registration

    def get_planeType(self):
        return self.planeType