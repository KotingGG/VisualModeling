import math

class Hydrogen:
    def __init__(self):
        self.name = "Hydrogen"
        self.symbol = "H"
        self.atomic_number = 1
        self.a0 = 0.529 
        self.scale = 100

        self.nucleus_radius_px = 5

    def get_name(self):
        return self.name

    def get_nucleus_radius_px(self):
        return self.nucleus_radius_px

    def get_orbit_radius_px(self):
        return int(self.a0 * self.scale)

    def probability_1s(self, x_ang, y_ang):
        r = math.sqrt(x_ang**2 + y_ang**2)
        return math.exp(-2*r/self.a0)

    def probability_2p(self, x_ang, y_ang, t):
        r = math.sqrt(x_ang**2 + y_ang**2)
        if r == 0:
            return 0
        
        angle_factor = (x_ang / r) ** 2
        radial_part = (r**2 / self.a0**2) * math.exp(-r/self.a0)
        time_factor = 0.5 + 0.5 * math.sin(t)
        
        return radial_part * angle_factor * time_factor * 0.1