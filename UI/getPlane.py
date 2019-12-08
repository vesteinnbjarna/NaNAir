from Model.plane import Plane

class GetPlane():
    def __init__(self, llAPI_in):
        self.llAPI_in  = llAPI_in

    def get_list(self):
        print()
        self.date = input("Enter date (mm/dd/yy): ")
        self.time = input("Enter time (hh:mm): ")
        print()
        # senda svo áfram date og time í data layer