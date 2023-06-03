import sys
import os

os.system("cls")
def print_numbers():
    count = 0
    for num in range(100, 201):
        if (num % 5 == 0 or num % 6 == 0) and not (num % 5 == 0 and num % 6 == 0):
            print(f"\033[1;32m{num}\033[0m", end=" ") 
            count += 1
            if count % 10 == 0:
                print()
    if count % 10 != 0:
        print()

def restart_program():
    while True:
        restart = input("Press Enter to restart or type (exit) to quit: ")
        if restart.lower() == 'exit':
            sys.exit(0)
        elif restart == '':
            os.system("cls")
            print_numbers()
        else:
            os.system("cls")
            print("Invalid input. Please try again.")

print("Welcome to the Number Printer!")
while True:
    os.system("cls")
    print_numbers()
    restart_program()
