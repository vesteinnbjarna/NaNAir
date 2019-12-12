class PlaneType():
    def __init__(self, planeType, manufacturer, seats):
        self.plane_type = planeType
        self.manufacturer = manufacturer
        self.seats = seats

    # def get_regis
    # tration (self):
    #     return self.registration

    def get_plane_type(self):
        return self.plane_type
    
    def get_manufacturer (self):
        return self.manufacturer

    def get_seats (self):
        return self.seats