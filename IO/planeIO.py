from IO.BaseClassIO import BaseClassIO
from Model.plane import Plane
from Model.PlaneType import PlaneType

class PlaneIO(BaseClassIO):

    def storePlaneToFile(self,plane_in):
        registration = Plane.get_registration(plane_in)
        planeType_obj = plane_in.get_planeType()
        planeType_str = planeType_obj.get_plane_type()
        
        plane_info = '\n{},{}'.format(registration,planeType_str)

        with open(self.filename,'a') as f:
            f.write(plane_info)
