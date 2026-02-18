class Hydrogen:
    def __init__(self):
        """
        Since the difference between the radius of the atom itself and the nucleus 
        of the atom with electrons is very huge (1:100,000), 
        we will round it off approximately for visualization.

        The ratio of the radius of an atom's nucleus to the radius of its electron is 1:10. 
        For clarity, this ratio has been changed to 1:2.
        """
        self.name = "Hydrogen"
        self.symbol = "H"
        self.nucleus_radius = 12.0
        self.electron_radius = 6.0
        self.orbit_radius = 0.529
        self.scale = 300

    def get_orbit_radius_px(self) -> float:
        """ Approximately rounded to `self.scale` for visualization """
        return self.orbit_radius * self.scale
    
    def get_nucleus_radius_px(self) -> float:
        return self.nucleus_radius
    
    def get_electron_radius_px(self) -> float:
        return self.electron_radius
    
    def get_name(self) -> str:
        return self.name