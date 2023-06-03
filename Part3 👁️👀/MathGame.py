import random
import os

while True:
    os.system("cls")
    num1 = random.randint(0, 99)
    num2 = random.randint(0, 99)

    print("\033[1;35m====================")
    print("\033[1;36mWelcome to the Math Game!")
    print("\033[1;35m====================\n")
    print(f"\033[1;32mWhat is {num1} * {num2}?")

    answer = int(input("\033[1;34mYour answer: "))

    correct_answer = num1 * num2

    if answer == correct_answer:
        print("\n\033[1;32mCorrect!")
    else:
        print("\n\033[1;31mIncorrect. The correct answer is", correct_answer)

    restart = input("\n\033[1;35mPress Enter to restart or type 'exit' to quit: ")
    if restart.lower() == "exit":
        break

print("\n\033[1;35m====================")
print("\033[1;36mThanks for playing!")
print("\033[1;35m====================")