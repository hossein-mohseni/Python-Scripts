import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen

    print("\033[1;34m" + "*** System of Equations Solver ***" + "\033[0m")

    # Input variables
    a, b, c, d, e, f = eval(input("\033[1;33m" + "Enter a, b, c, d, e, f: " + "\033[0m"))

    # Calculate determinant
    determinant = a * d - b * c

    if determinant == 0:
        print("\033[1;31m" + "The system of equations has no solution." + "\033[0m")
    else:
        # Calculate x and y
        x = (e * d - b * f) / determinant
        y = (a * f - e * c) / determinant

        # Print results
        print("\033[1;32m" + "x is:", str(x), "y is:", str(y) + "\033[0m")

    restart = input("\n\033[1;36m" + "Press Enter to Restart or 'q' to Quit: " + "\033[0m")
    if restart.lower() == 'q':
        break