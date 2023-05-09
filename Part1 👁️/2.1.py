def Baner():
    print("|+++++++++++++++++++++++++++++++++++++++++++++++++|")
    print("|             _        _                          |")
    print("|       /\   (_)      | |                         |")
    print("|      /  \   _ _ __  | |_ ___ _ __ ___  _ __     |")
    print("|     / /\ \ | | '__| | __/ _ \ '_ ` _ \| '_ \    |")
    print("|    / ____ \| | |    | ||  __/ | | | | | |_) |   |")
    print("|   /_/    \_\_|_|     \__\___|_| |_| |_| .__/    |")
    print("|                                       | |       |")
    print("|                                       |_|       |")
    print("|                                                 |")
    a = input("|-------[Enter the temperature in Celsius]--------|\n|---->> ")
    return a

print("|----[Air temperature in Fahrenheit]---->> ", (9 / 5) * float(Baner()) + 32)