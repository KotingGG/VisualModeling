import os
import math
import time

class Donut:
    # ASCII canvas dimensions
    SCREEN_WIDTH = 50
    SCREEN_HEIGHT = 50

    # Angle steps
    THETA_SPACING = 0.07
    PHI_SPACING = 0.02

    # Geometry of the torus
    R1 = 1          # tube radius
    R2 = 2          # distance from center to center of tube
    K2 = 5          # distance to observer

    # Projection ratio (calculated automatically based on screen size)
    K1 = SCREEN_WIDTH * K2 * 3 / (8 * (R1 + R2))

    # Illumination symbol set (from dark to light)
    CHARSET = ".,-~:;=!*#$@"

    @staticmethod
    def run():
        """Starts an endless animation of a rotating torus."""
        A = 0.0  # rotation angle around the X axis
        B = 0.0  # rotation angle around the Z axis
        try:
            while True:
                Donut.render_frame(A, B)
                A += 0.04
                B += 0.02
                time.sleep(0.03)
        except KeyboardInterrupt:
            print("\nAnimation stopped by user.")

    @staticmethod
    def render_frame(A, B):
        """Draws one frame of a torus at the given angles A and B."""
        cosA = math.cos(A)
        sinA = math.sin(A)
        cosB = math.cos(B)
        sinB = math.sin(B)

        # Screen buffers and z-buffer
        output = [[' ' for _ in range(Donut.SCREEN_WIDTH)] for _ in range(Donut.SCREEN_HEIGHT)]
        zbuffer = [[0.0 for _ in range(Donut.SCREEN_WIDTH)] for _ in range(Donut.SCREEN_HEIGHT)]

        # Angle theta is along the torus tube
        theta = 0.0
        while theta < 2 * math.pi:
            costheta = math.cos(theta)
            sintheta = math.sin(theta)

            # Angle phi - around the central axis of the torus
            phi = 0.0
            while phi < 2 * math.pi:
                cosphi = math.cos(phi)
                sinphi = math.sin(phi)

                circlex = Donut.R2 + Donut.R1 * costheta
                circley = Donut.R1 * sintheta

                x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
                y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
                z = Donut.K2 + cosA * circlex * sinphi + circley * sinA

                ooz = 1 / z

                xp = int(Donut.SCREEN_WIDTH / 2 + Donut.K1 * ooz * x)
                yp = int(Donut.SCREEN_HEIGHT / 2 - Donut.K1 * ooz * y)

                # Calculate the brightness (the scalar product of the normal and the light direction)
                L = (cosphi * costheta * sinB -
                     cosA * costheta * sinphi -
                     sinA * sintheta +
                     cosB * (cosA * sintheta - costheta * sinA * sinphi))

                # If the point is turned towards us and hits the screen
                if L > 0 and 0 <= xp < Donut.SCREEN_WIDTH and 0 <= yp < Donut.SCREEN_HEIGHT:
                    if ooz > zbuffer[yp][xp]:
                        zbuffer[yp][xp] = ooz
                        luminance_index = int(L * 8) # from 0 to 11
                        if 0 <= luminance_index < len(Donut.CHARSET):
                            output[yp][xp] = Donut.CHARSET[luminance_index]

                phi += Donut.PHI_SPACING
            theta += Donut.THETA_SPACING

        # Clearing the screen and displaying the frame
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in output:
            print(''.join(row))