import os

def print_banner():
    print("\033[1;31;40m")
    print("**********************************************")
    print("***                                        ***")
    print("***        Sum of Digits Calculator        ***")
    print("***                                        ***")
    print("**********************************************\n")
    print("\033[0m")

while True:
    os.system("cls")
    # Print the banner
    print_banner()
    
    # Get user input
    num = int(input("Enter an integer [-1 to exit] >>> "))

    # Exit if user enters -1
    if num == -1:
        break

    # Extracting digits using % operator and summing them up
    sum_of_digits = 0
    while num > 0:
        sum_of_digits += num % 10
        num //= 10

    # Display the result
    print("\033[1;32;40m")
    print("The sum of the digits is >>", sum_of_digits, "\n")
    print("\033[0m")
    
    input("Press Enter to Restart ...")
