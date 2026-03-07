from Cube.cube import Cube
from Donut.donut import Donut

def main():

    while True:
        model = input("Select model (cube/donut): ").strip().lower()
        if model in ("cube", "donut"):
            break
        print("Invalid input. Please enter 'cube' or 'donut'.")

    print("\x1b[2J") # Cleaning the screen

    if model == "cube":
        Cube.run()
    else:
        Donut.run()

if __name__ == "__main__":
    main()