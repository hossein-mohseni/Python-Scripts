import os

while True:
    os.system("cls")
    decimal_int = int(input("\033[1;32mEnter an integer between 0 and 15: \033[0m"))
    
    if 0 <= decimal_int <= 15:
        hex_num = hex(decimal_int)[2:].upper()
        print("\033[1;34mThe hexadecimal equivalent of", decimal_int, "is", hex_num, "\033[0m")
    else:
        print("\033[1;31mInvalid input! Please enter an integer between 0 and 15.\033[0m")
    
    input("\033[1;33mPress Enter to Restart...\033[0m")
