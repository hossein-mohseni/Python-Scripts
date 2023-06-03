from colorama import Fore, Style
import os

while True:
    os.system("cls")
    positive_count = 0
    negative_count = 0
    total = 0
    count = 0

    while True:
        number = int(input("Enter an integer (0 to end): "))

        if number == 0:
            break

        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1

        total += number
        count += 1

    if count > 0:
        average = total / count
        print(Fore.GREEN + "Positive numbers count:", positive_count)
        print(Fore.RED + "Negative numbers count:", negative_count)
        print(Fore.BLUE + "Total:", total)
        print(Fore.YELLOW + "Average:", average)
    else:
        print(Fore.RED + "No numbers were entered.")

    restart = input(Fore.CYAN + "\nPress Enter to Restart, or enter 'q' to quit: ")
    print(Style.RESET_ALL)

    if restart.lower() == 'q':
        break
