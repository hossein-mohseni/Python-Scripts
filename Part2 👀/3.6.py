import os
import time

while True:
    os.system("cls")
    # Display banner and get input from user
    print('\033[1m' + '\033[95m' + '\n       ASCII CONVERTER' + '\033[0m')
    ascii_code = input('\033[96m' + '\nEnter a number between 0 and 127: ' + '\033[0m')

    # Check the validity of input and convert to character
    if ascii_code.isdigit() and int(ascii_code) in range(128):
        character = chr(int(ascii_code))
        # Display the result with a header
        os.system("cls")
        print('\n' + '\033[1m' + '\033[92m' + '       ASCII CONVERSION' + '\033[0m')
        print('\nASCII code:', '\033[96m', ascii_code, '\033[0m')
        print('Character:', '\033[93m', character, '\033[0m')
        input("\nPress Enter to Restart...")
    else:
        os.system("cls")
        print("\033[91m" + "Invalid input. Please enter a number between 0 and 127." + "\033[0m")
        time.sleep(3)
        continue

