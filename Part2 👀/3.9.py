import os

while True:
    os.system("cls")
    # ANSI escape sequences for colors
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    reset = "\033[0m"

    # Print the banner
    print(f"{red}#####   Payroll Statement   #####{reset}")
    print(f"\n\n{green}Enter Employee Information Below{reset}")

    # Get input from user
    name = input(f"{yellow}Enter employee's name:{reset} ")
    hours_worked = float(input(f"{blue}Enter number of hours worked in a week:{reset} "))
    hourly_rate = float(input(f"{blue}Enter hourly pay rate:{reset} "))
    federal_tax_rate = float(input(f"{blue}Enter federal tax withholding rate (%):{reset} ")) / 100
    state_tax_rate = float(input(f"{blue}Enter state tax withholding rate (%):{reset} ")) / 100

    # Calculate payroll information
    gross_pay = hours_worked * hourly_rate
    federal_withholding = gross_pay * federal_tax_rate
    state_withholding = gross_pay * state_tax_rate
    total_withholding = federal_withholding + state_withholding
    net_pay = gross_pay - total_withholding

    os.system("cls")
    # Print the payroll statement
    print(f"{purple}Deductions:{reset}")
    print(f"\nPayroll statement for {purple}{name}{reset}")
    print(f"Hours worked: {green}{hours_worked:.2f}${reset}")
    print(f"Hourly pay rate: {green}{hourly_rate:.2f}${reset}")
    print(f"Gross pay: {green}{gross_pay:.2f}${reset}")
    print(f"Federal withholding amount: {yellow}{federal_withholding:.2f}${reset}")
    print(f"State withholding amount: {yellow}{state_withholding:.2f}${reset}")
    print(f"Total withholding amount: {yellow}{total_withholding:.2f}${reset}")
    print(f"Net pay: {red}{net_pay:.2f}${reset}")
    input("\nPress Enter to Restart Payroll Statement...")
