class PlaneType():
    def __init__(self, plane_type, manufacturer, model, seats):
        self.plane_type = plane_type
        self.manufacturer = manufacturer
        self.model = model
        self.seats = seats 

    def get_plane_type(self):
        return self.plane_type
    
    def get_manufacturer (self):
        return self.manufacturer

    def get_model(self):
        return self.model

    def get_seats (self):
        return self.seats