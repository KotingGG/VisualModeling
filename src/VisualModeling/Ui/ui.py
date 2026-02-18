import customtkinter as ctk
import math

from ..Atom.hydrogen import Hydrogen

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ctk.set_appearance_mode("Dark")

        self.atom = Hydrogen()

        self.title(f"Visual Modeling: {self.atom.get_name()}")
        self.canvas = ctk.CTkCanvas(
            self, 
            width=800, 
            height=600, 
            bg='#3c3c3c', 
            highlightthickness=0
        )
        self.canvas.pack(fill='both', expand=True)

        self.angle = 0.0

        self.after(100, self.draw_atom) # Wait for canvas to render



    def draw_atom(self):
        cx, cy = self.get_canvas_center()
        nr_px = self.atom.get_nucleus_radius_px()
        or_px = self.atom.get_orbit_radius_px()
        er_px = self.atom.get_electron_radius_px()

        # Nucleus 
        self.nucleus = self.canvas.create_oval(
            cx - nr_px,
            cy - nr_px, 
            cx + nr_px, 
            cy + nr_px, 
            fill='red', 
            outline="grey"  
        )

        # Orbit (only 1)
        self.orbit = self.canvas.create_oval(
            cx - or_px, 
            cy - or_px, 
            cx + or_px, 
            cy + or_px, 
            outline="white"  
        )

        # Electron
        ex = cx + or_px
        ey = cy
        self.electron = self.canvas.create_oval(
            ex - er_px, 
            ey - er_px, 
            ex + er_px, 
            ey + er_px,
            fill='blue'
        )

        self.animate()



    def animate(self):
         self.angle += 0.05
         cx, cy = self.get_canvas_center()
         or_px = self.atom.get_orbit_radius_px()

         x = cx + or_px * math.cos(self.angle)
         y = cy + or_px * math.sin(self.angle)
    
         self.canvas.coords(self.electron, x-5, y-5, x+5, y+5)
    
         self.after(20, self.animate)



    def get_canvas_center(self):
        self.update_idletasks()
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        return w//2, h//2