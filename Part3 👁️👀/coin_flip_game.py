import random
import os
 
outcomes = ["head", "tail"]

while True:
    os.system("cls")
    coin_flip = random.randint(0, 1)

    user_guess = int(input("\nGuess the coin flip (0 for head, 1 for tail): "))

    if user_guess == coin_flip:
        print("\nCongratulations! It's", outcomes[coin_flip] + ". You guessed correctly!")
    else:
        print("\nSorry, it's", outcomes[coin_flip] + ". You guessed incorrectly.")

    restart = input("\nPress Enter to restart or type 'exit' to quit: ")
    if restart.lower() == 'exit':
        break
