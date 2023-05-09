import os
import time

while True:
    os.system('cls')
    # Define a function to print a banner with a given message
    def print_banner(message):
        banner_width = len(message) + 6
        print("=" * banner_width)
        print("|", " " * (banner_width - 4), "|")
        print(f"|  {message}  |")
        print("|", " " * (banner_width - 4), "|")
        print("=" * banner_width)

    # Print banner with welcome message
    print_banner("Welcome to the Cylinder Volume Calculator!")

    # Get input for radius and length of cylinder, and convert to float values
    radius, length = map(float, input("\nPlease enter the radius and length of the cylinder (separated by space): ").split())

    # Calculate area and volume of cylinder using formulas
    area = radius ** 2 * 3.14159
    volume = area * length

    # Print formatted output with calculated results
    os.system('cls')
    print_banner("Welcome to the Cylinder Volume Calculator!")
    print("\nCalculating...\n")
    time.sleep(3)
    os.system('cls')
    print_banner("Welcome to the Cylinder Volume Calculator!")
    print(f"\nThe area of the cylinder with radius {radius:.1f} and length {length:.1f} is {area:.2f}.")
    print(f"The volume of the cylinder is {volume:.2f}.\n")
    input("Press Enter to restart the calculation...")

