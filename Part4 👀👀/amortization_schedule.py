import os
 
def calculate_amortization_schedule(loan_amount, num_years, interest_rate):
    monthly_interest_rate = interest_rate / 12 / 100
    num_months = num_years * 12
    monthly_payment = loan_amount * monthly_interest_rate / (1 - 1 / (1 + monthly_interest_rate) ** num_months)

    print("\nAmortization Schedule")
    print("---------------------")
    print("Loan Amount: $", loan_amount)
    print("Number of Years: ", num_years)
    print("Interest Rate: ", interest_rate, "%")
    print("Monthly Payment: $", round(monthly_payment, 2))
    print("---------------------")
    print("Payment\t\tInterest\tPrincipal\tBalance")

    balance = loan_amount
    for payment in range(1, num_months + 1):
        monthly_interest = balance * monthly_interest_rate
        principal = monthly_payment - monthly_interest
        balance -= principal

        print(payment, "\t\t", round(monthly_interest, 2), "\t\t", round(principal, 2), "\t\t", round(balance, 2))


def main():
    while True:
        os.system("cls")
        loan_amount = float(input("Enter the loan amount: "))
        num_years = int(input("Enter the number of years: "))
        interest_rate = float(input("Enter the interest rate (%): "))

        calculate_amortization_schedule(loan_amount, num_years, interest_rate)

        restart = input("\nPress Enter to restart or type 'exit' to quit: ")
        if restart.lower() == "exit":
            break


if __name__ == '__main__':
    main()
