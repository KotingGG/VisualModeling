import customtkinter as ctk
import math
import random

from hydrogen import Hydrogen

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        """
        Initializes the main window of the application.
        """
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

        self.grid_size = 200
        self.angle = 0.0
        self.time = 0
        self.dt = 0.1
        self.animate_after_id = None

        self.after(1, self.draw_atom)

    def draw_atom(self):
        """
        Triggers the construction of a static probability cloud and 
        starts the animation if it hasn't already started.
        """
        self.draw_probability_cloud()

        if not hasattr(self, 'animate_after_id') or self.animate_after_id is None:
            self.animate()

    def draw_probability_cloud(self):
        """
        Draws a probability cloud for the 1s state with improved visualization:
        - dot size depends on the probability;
        - color smoothly changes from blue (low probability) to yellow/white;
        - random noise is added to break the regularity of the grid;
        - even very small probabilities (outliers) are displayed as small dots.
        """
        self.canvas.delete("all")
        cx, cy = self.get_canvas_center()

        step_angstrom = 2.0 / (self.grid_size // 2)
        step_px = step_angstrom * self.atom.scale

        max_prob = 0.0
        points = []  # list of tuples (x_px, y_px, prob)

        # First, we collect all the points and look for the maximum probability
        for i in range(-self.grid_size//2, self.grid_size//2):
            for j in range(-self.grid_size//2, self.grid_size//2):
                x_ang = i * step_angstrom
                y_ang = j * step_angstrom
                prob = self.atom.probability_1s(x_ang, y_ang)
                if prob > max_prob:
                    max_prob = prob

                x_px = cx + i * step_px
                y_px = cy + j * step_px
                points.append((x_px, y_px, prob))

        # Add random noise to the coordinates (spread up to half a step)
        noise_range = step_px * 0.1

        for x_px, y_px, prob in points:
            # Adding noise
            nx = x_px + random.uniform(-noise_range, noise_range)
            ny = y_px + random.uniform(-noise_range, noise_range)

            norm_prob = prob / max_prob if max_prob > 0 else 0

            radius = 5 + 4 * norm_prob

            # Color: smooth transition from blue (norm_prob=0) to yellow/white (norm_prob=1)
            # Using HSV-like logic: from blue (240°) through magenta to red/yellow
            # For simplicity, we'll use linear interpolation between RGB
            if norm_prob < 0.5:
                # from blue to purple
                t = norm_prob * 2
                r = int(100 * t)
                g = 0
                b = 255
            else:
                # from magenta to yellow/white
                t = (norm_prob - 0.5) * 2
                r = 255
                g = int(200 * t)
                b = int(255 * (1 - t))

            # Increase brightness for higher probabilities
            color = f'#{r:02x}{g:02x}{b:02x}'

            # Draw a dot (you can add translucency via stipple, but Tkinter doesn't support alpha)
            self.canvas.create_oval(
                nx - radius, ny - radius,
                nx + radius, ny + radius,
                fill=color, outline=''
            )

        # Nucleus of an atom
        self.canvas.create_oval(
            cx - 5, cy - 5, cx + 5, cy + 5,
            fill='red', outline='white'
        )

    def draw_animated_probability(self):
        """
        Draws an animated probability cloud (mix of 1s and 2p)
        """
        self.canvas.delete("all")
        cx, cy = self.get_canvas_center()

        step_angstrom = 2 / 20
        step_px = step_angstrom * self.atom.scale

        max_prob = 0.0
        points = []

        rot_angle = self.time * 0.5

        for i in range(-60, 60):
            for j in range(-60, 60):
                x_ang = i * step_angstrom
                y_ang = j * step_angstrom
                prob_1s = self.atom.probability_1s(x_ang, y_ang)

                x_rot = x_ang * math.cos(rot_angle) - y_ang * math.sin(rot_angle)
                y_rot = x_ang * math.sin(rot_angle) + y_ang * math.cos(rot_angle)
                prob_2p = self.atom.probability_2p(x_rot, y_rot, self.time)

                prob = prob_1s * 0.6 + prob_2p * 0.4
                if prob > max_prob:
                    max_prob = prob
                x_px = cx + i * step_px
                y_px = cy + j * step_px
                points.append((x_px, y_px, prob))

        for x_px, y_px, prob in points:
            nx, ny = x_px, y_px

            norm_prob = prob / max_prob if max_prob > 0 else 0

            if norm_prob < 0.0075:
                continue

            radius = 2 + 5 * norm_prob

            if norm_prob < 0.5:
                t = norm_prob * 2
                r = int(80 + 80 * t)
                g = int(30 * t)
                b = 255 - int(50 * t)
            else:
                t = (norm_prob - 0.5) * 2
                r = 255
                g = int(150 + 105 * t)
                b = int(200 * (1 - t))

            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_oval(
                nx - radius, ny - radius,
                nx + radius, ny + radius,
                fill=color, outline=''
            )

        self.canvas.create_oval(
            cx - self.atom.get_nucleus_radius_px(),
            cy - self.atom.get_nucleus_radius_px(),
            cx + self.atom.get_nucleus_radius_px(),
            cy + self.atom.get_nucleus_radius_px(),
            fill='yellow',
            outline='white'
        )

    def animate(self):
        self.draw_animated_probability()
        self.time += self.dt
        self.animate_after_id = self.after(300, self.animate)

    def get_canvas_center(self):
        """
        Returns the coordinates of the canvas center (integers).
        Updates the geometry before measuring to get the current dimensions.
        """
        self.update_idletasks()
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        return w//2, h//2