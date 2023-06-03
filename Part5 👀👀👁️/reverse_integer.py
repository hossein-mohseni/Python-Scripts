from colorama import init, Fore
import os
 
def reverse(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number //= 10
    return reversed_number

init(autoreset=True)

while True:
    os.system("cls")
    try:
        integer = int(input(Fore.CYAN + "Enter an integer: "))
        reversed_integer = reverse(integer)
        print(Fore.GREEN + "Reversed integer:", reversed_integer)
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter an integer.")
    
    restart = input(Fore.YELLOW + "\nPress Enter to Restart or enter 'q' to quit: ")
    if restart.lower() == 'q':
        break
