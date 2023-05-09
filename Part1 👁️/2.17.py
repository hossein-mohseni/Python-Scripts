import os

while True:
    os.system("cls")
    # Prompt user to input weight and height
    print('\033[1m' + '\033[95m' + '       BMI CALCULATOR' + '\033[0m')
    weight_pounds = float(input('\033[96m' + '\nEnter your weight in pounds: ' + '\033[0m'))
    height_inches = float(input('\033[93m' + 'Enter your height in inches: ' + '\033[0m'))

    # Calculate BMI
    weight_kg = weight_pounds * 0.45359237
    height_meters = height_inches * 0.0254
    bmi = round(weight_kg / (height_meters ** 2), 2)

    os.system("cls")
    # Print the result with a header
    print('\n' + '\033[1m' + '\033[92m' + '       BMI RESULTS' + '\033[0m')
    print('\nYour weight:', '\033[96m', weight_pounds, 'pounds', '\033[0m', '(', '\033[95m', weight_kg, 'kg', '\033[0m', ')')
    print('Your height:', '\033[93m', height_inches, 'inches', '\033[0m', '(', '\033[94m', height_meters, 'm', '\033[0m', ')')
    print('Your BMI:', '\033[91m', bmi, '\033[0m')
    input("\nPress Entter to Restart...")
