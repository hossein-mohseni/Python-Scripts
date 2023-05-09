import random
import os

while True:
    os.system("cls")
    # Generate a random uppercase letter
    random_letter = chr(random.randint(65, 90))
    os.system("cls")
    # Display the result with a header
    print('\n' + '\033[1m' + '\033[92m' + '       RANDOM UPPERCASE LETTER' + '\033[0m')
    print('\nGenerated letter >>> ', '\033[93m', random_letter, '\033[0m')
    input("\nPress Enter to Restart the script ...")
