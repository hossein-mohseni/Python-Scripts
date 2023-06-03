from colorama import init, Fore
import os
 
init() 
while True:
    os.system("cls")
    try:
        num1, num2, num3 = map(int, input("Enter three integers separated by commas: ").split(","))

        minimum = min(num1, num2, num3)
        maximum = max(num1, num2, num3)
        middle = (num1 + num2 + num3) - minimum - maximum

        print(Fore.GREEN + "The integers in increasing order are:", minimum, middle, maximum)
        print(Fore.RESET)

        input(Fore.BLUE + "Press Enter to Restart" + Fore.RESET)
    except ValueError:
        print(Fore.RED + "Invalid input! Please enter three integers separated by commas." + Fore.RESET)
