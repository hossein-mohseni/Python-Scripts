import math
import os

while True:
    os.system("cls")
    # Display banner and get input from user
    print('\n\033[1m' + '\033[95m' + '       PENTAGON AREA CALCULATOR' + '\033[0m')
    r = float(input('\033[96m' + '\nEnter the length from the center of a pentagon: ' + '\033[0m'))

    # Calculate the area of the pentagon
    s = 2 * r * math.sin(math.pi/5)
    area = (3 * math.sqrt(3) / 2) * s**2 

    # Display the result with a header
    os.system("cls")
    print('\n' + '\033[1m' + '\033[92m' + '       AREA OF THE PENTAGON' + '\033[0m')
    print('\nLength from the center:', '\033[96m', r, '\033[0m')
    print('Side length:', '\033[92m', "{:.2f}".format(s), '\033[0m')
    print('Area:', '\033[94m', "{:.2f}".format(area), '\033[0m')
    input("\nPress Entter to Restart...")
