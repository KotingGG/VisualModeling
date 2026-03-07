class Cube:
    @staticmethod
    def run():

        while True:
            try:
                Cube.render_frame()
            except KeyboardInterrupt:
                print("\nThe program was terminated by the user")
                exit()

    @staticmethod
    def render_frame():

        print("Cube")

        print("\x1b[H") # moves the terminal cursor to the upper left corner (position 0,0).