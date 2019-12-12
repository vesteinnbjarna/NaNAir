from IO.BaseClassIO import BaseClassIO
<<<<<<< HEAD
from Model.plane import Plane
=======
from Model.Plane import Plane
from Model.PlaneType import PlaneType
>>>>>>> 7b34e934b10d1615029a9be8622aa814fc3aee49

class PlaneIO (BaseClassIO):
    #def __init__(self,filename):
    #    self.planeFileName = filename
        

    def loadPlanesFromFiles(self):
        pass

    def storePlaneToFile(self,plane_in):
        registration = Plane.get_registration(plane_in)
        seats = PlaneType.get_seats(plane_in)
        manufacturer = PlaneType.get_manufacturer(plane_in)
        plane_type = Plane.get_plane_type(plane_in)
        
        plane_info = '\n{},{}'.format(registration,plane_type)

        with open(self.filename,'a') as f:
            f.write(plane_info)
