import colorama
from colorama import Fore, Style
import os

def display_number_pyramid():
    size = 5

    for i in range(size):
        for j in range(size - i - 1):
            print(' ', end=' ')

        for j in range(i + 1):
            if j % 2 == 0:
                print(Fore.RED + str(j + 1), end=' ')
            else:
                print(Fore.BLUE + str(j + 1), end=' ')

        for j in range(i, 0, -1):
            if j % 2 == 0:
                print(Fore.RED + str(j), end=' ')
            else:
                print(Fore.BLUE + str(j), end=' ')

        print(Style.RESET_ALL)

colorama.init()
restart = True

while restart:
    os.system('cls')
    display_number_pyramid()
    input("\nPress Enter to Restart or type 'exit' to quit: ")
    restart = False if input().lower() == 'exit' else True
