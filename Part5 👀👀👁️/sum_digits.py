import time
import os 

def sumDigits(n):
    total = 0
    while n != 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

while True:
    os.system("cls")
    print("\n--- Sum of Digits Calculator ---\n")
    integer = int(input("Enter an integer: "))

    result = sumDigits(integer)
    print("Sum of digits:", result)

    restart = input("\nPress Enter to restart or 'q' to quit: ")
    if restart.lower() == 'q':
        print("\nThank you for using the Sum of Digits Calculator. Goodbye!")
        break
    
    print("\nRestarting...")
    time.sleep(1)  # Adds a delay of 1 second before restarting the loop
