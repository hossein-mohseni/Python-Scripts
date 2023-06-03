import time
import os

while True:
    os.system("cls")
    hex_char = input("\nEnter a hex character: ")

    decimal_int = int(hex_char, 16)

    print("\n\033[1;32mThe decimal equivalent of", hex_char, "is", decimal_int, "\033[0m")

    input("\n\033[1;34mPress Enter to Restart\033[0m")
    print("\033c", end='')  # Clear the console

    # Delay for a better user experience
    time.sleep(0.5)