from math import acos, radians, sin, cos
import os

while True:
    os.system("cls")
    # Display banner and get input from user
    print('\033[1m' + '\033[95m' + '       GREAT CIRCLE DISTANCE CALCULATOR' + '\033[0m')
    lat_lon1 = input('\033[96m' + 'Enter the latitude and longitude of the first point (in degrees): ' + '\033[0m')
    lat_lon2 = input('\033[93m' + 'Enter the latitude and longitude of the second point (in degrees): ' + '\033[0m')
    x1, y1 = map(radians, map(float, lat_lon1.split(',')))
    x2, y2 = map(radians, map(float, lat_lon2.split(',')))

    # Calculate great circle distance
    radius = 6371.01
    d = radius * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))

    os.system("cls")
    # Display the result with a header
    print('\n' + '\033[1m' + '\033[92m' + '       GREAT CIRCLE DISTANCE' + '\033[0m')
    print('Latitude and longitude of first point:', '\033[96m', lat_lon1, '\033[0m')
    print('Latitude and longitude of second point:', '\033[93m', lat_lon2, '\033[0m')
    print('Great circle distance:', '\033[94m', "{:.2f}".format(d), 'km', '\033[0m')
    input("\nPress Enter to Restart...")