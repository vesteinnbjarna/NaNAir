from IO.BaseClassIO import BaseClassIO
from Model.PlaneType import PlaneType

class PlaneTypeIO(BaseClassIO):

    def storePlaneTypeToFile(self, type_in):
        planeType = type_in.get_plane_type()
        manufacturer = type_in.get_manufacturer()
        model = type_in.get_model()
        seats = type_in.get_seats()