import time
import os

while True:
    os.system("cls")
    i = 1
    while i < 7:
        print("\033[1;3{}m{}\033[0m".format(i, i * "*"))
        i += 1
        time.sleep(0.1)  # Add a small delay for better visualization
    
    input("\nPress Enter to Restart")
