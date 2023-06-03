import random
import os
 
def printMatrix(n):
    for _ in range(n):
        row = ' '.join(str(random.choice([0, 1])) for _ in range(n))
        print(f"\033[0;{random.randint(31, 36)}m{row}\033[0m")

while True:
    os.system("cls")
    n = int(input("Enter the value of n: "))
    print("Matrix:")
    printMatrix(n)

    input("Press Enter to Restart or Ctrl+C to exit...")
