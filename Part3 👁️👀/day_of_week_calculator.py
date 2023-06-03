import time
import os

while True:
    os.system("cls")
    print("\n--- Day of the Week Calculator ---\n")
    
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day of the month: "))

    if month == 1 or month == 2:
        month += 12
        year -= 1

    h = (day + (13 * (month + 1) // 5) + year + (year // 4) - (year // 100) + (year // 400)) % 7

    days_of_week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    day_of_week = days_of_week[h]

    print("\nCalculating...\n")
    time.sleep(1)

    print("\033[1mThe day of the week for {}/{}/{} is {}.\033[0m".format(month, day, year, day_of_week))

    restart = input("\nPress Enter to restart or 'q' to quit: ")
    if restart.lower() == 'q':
        break
