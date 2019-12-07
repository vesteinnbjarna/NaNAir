class Plane():
    def __init__(self, registration, plane_type, manufacturer, seats):
        self.registration = registration
        self.plane_type = plane_type
        self.manufacturer = manufacturer
        self.seats = seats

    def get_registration (self):
        return self.registration

    def get_plane_type(self):
        return self.plane_type
    
    def get_manufacturer (self):
        return self.manufacturer

    def get_seats (self):
        return self.seats