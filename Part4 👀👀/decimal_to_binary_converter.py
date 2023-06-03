import os

def decimal_to_binary():
    while True:
        os.system('cls')
        decimal = eval(input("\nEnter a decimal integer: "))
        binary = bin(decimal)[2:]
        print("\nBinary representation:", '\033[1;32m' + binary + '\033[0m')
        
        input("\nPress Enter to Restart...")

decimal_to_binary()