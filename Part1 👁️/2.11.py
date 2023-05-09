import os

def main():
    os.system("cls")
    # Get final account value from the user
    final_value = float(input("\033[96mEnter the final account value: \033[0m"))

    # Get annual interest rate from the user
    annual_rate = float(input("\033[95mEnter the annual interest rate: \033[0m"))

    # Get number of years from the user
    years = int(input("\033[94mEnter the number of years: \033[0m"))

    # Calculate monthly interest rate and initial deposit
    monthly_interest_rate = annual_rate / 1200
    initial_deposit = final_value / ((1 + monthly_interest_rate) ** (years * 12))

    # Print the initial deposit value rounded to two decimal places
    print("\033[92mThe initial deposit value is:\033[0m", "\033[1m", round(initial_deposit, 2), "\033[0m")

    input("press Enter")
    main()

while True:
    main()