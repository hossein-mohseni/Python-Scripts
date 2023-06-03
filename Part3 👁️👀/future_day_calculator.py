import time
import os
 
while True:
    os.system("cls")
    today = int(input("\nEnter today's day (0-6): "))
    days_after = int(input("Enter the number of days elapsed since today: "))

    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    future_day = (today + days_after) % 7

    print("\nThe future day is", days_of_week[future_day])

    print("\nPress Enter to Restart or type 'exit' to quit.")
    restart = input()

    if restart == "exit":
        break
    else:
        print("\nRestarting...")
        time.sleep(1)
