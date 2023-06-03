import random
import os

while True:
    os.system("cls")
    user_choice = int(input("Enter your choice (0 for scissor, 1 for rock, 2 for paper): "))

    computer_choice = random.randint(0, 2)

    choices = ["scissor", "rock", "paper"]

    print("\nYou chose", choices[user_choice])
    print("Computer chose", choices[computer_choice])

    if user_choice == computer_choice:
        print("\nIt's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("\nYou win!")
    else:
        print("\nSorry, you lose!")

    restart = input("\nPress Enter to restart or type 'q' to quit: ")
    if restart.lower() == 'q':
        break

print("Thank you for playing!")