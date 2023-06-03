import time
import os
 
def compute_approximation():
    while True:
        os.system("cls")
        for i in range(10000, 100001, 10000):
            result = 0
            for j in range(1, i + 1):
                result += ((-1) ** (j + 1)) / (2 * j - 1)
            approximation = 4 * result
            print(f"\033[94mi = {i}: Approximation = {approximation}\033[0m")
        
        restart = input("\nPress Enter to Restart or type 'exit' to quit: ")
        if restart.lower() == "exit":
            break
        print("Restarting...\n")
        time.sleep(1)

compute_approximation()
