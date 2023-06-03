from termcolor import colored
import os
 
def displaySortedNumbers(num1, num2, num3):
    sorted_numbers = sorted([num1, num2, num3])
    sorted_string = ' '.join(str(num) for num in sorted_numbers)
    sorted_string = colored(sorted_string, 'green')
    print("Numbers in increasing order:")
    print(sorted_string)

while True:
    os.system("cls")
    num1, num2, num3 = eval(input("Enter the first number: "))

    displaySortedNumbers(num1, num2, num3)

    restart = input("Press Enter to restart or enter 'q' to quit: ")
    if restart.lower() == 'q':
        break
