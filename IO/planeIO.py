from IO.BaseClassIO import BaseClassIO
from Model.plane import Plane

class PlaneIO (BaseClassIO):
    #def __init__(self,filename):
    #    self.planeFileName = filename
        

    def loadPlanesFromFiles(self):
        pass

    def storePlaneToFile(self,plane_in):
        registration = Plane.get_registration(plane_in)
        seats = Plane.get_seats(plane_in)
        manufacturer = Plane.get_manufacturer(plane_in)
        plane_type = Plane.get_plane_type(plane_in)
        
        plane_info = '\n{},{},{},{}'.format(plane_type,manufacturer,registration,seats)

        with open(self.filename,'a') as f:
            f.write(plane_info)
