import colorama
from colorama import Fore, Style
import os

def display_ascii_table():
    start_char = ord('!')
    end_char = ord('~')
    chars_per_line = 10
    colorama.init()

    while True:
        os.system('cls')
        for char_code in range(start_char, end_char + 1):
            print(Fore.GREEN + chr(char_code) + Style.RESET_ALL, end=' ')
            if (char_code - start_char + 1) % chars_per_line == 0:
                print()
        print()
        user_input = input("Press Enter to Restart or type 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        print()

display_ascii_table()
