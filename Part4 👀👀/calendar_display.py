import calendar
import os

def display_calendar():
    while True:
        os.system("cls")
        year = int(input("Enter the year: "))
        first_day = int(input("Enter the first day of the year (0 for Monday, 1 for Tuesday, and so on): "))

        for month in range(1, 13):
            cal = calendar.monthcalendar(year, month)

            month_name = calendar.month_name[month]

            print(f"\n{month_name} {year}")

            print("\033[1mMon Tue Wed Thu Fri Sat Sun\033[0m")

            starting_day = (first_day + 1) % 7

            for week in cal:
                line = ""
                for day in week:
                    if day == 0:
                        line += "    "
                    else:
                        line += f"\033[94m{day:3d}\033[0m "
                print(line)

            first_day = (first_day + calendar.monthrange(year, month)[1]) % 7

        restart = input("\nPress Enter to restart or enter 'q' to quit: ")
        if restart.lower() == 'q':
            break
        print()

display_calendar()
