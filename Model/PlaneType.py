class PlaneType():
<<<<<<< HEAD
    def __init__(self, planeType, manufacturer, seats):
        self.plane_type = planeType
=======
    def __init__(self, plane_type, manufacturer, model, seats):
        self.plane_type = plane_type
>>>>>>> a1dab497258b4bd279a0de7f825271fa6b140d80
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