import colorama
from colorama import Fore, Style
import os

colorama.init(autoreset=True)
while True:
    os.system("cls")
    # Define banner text
    banner = r"""  
     _   _                                                _             
    | | (_)                                              | |            
    | |_ _ _ __ ___   ___    ___ ___  _ ____   _____ _ __| |_ ___  _ __ 
    | __| | '_ ` _ \ / _ \  / __/ _ \| '_ \ \ / / _ \ '__| __/ _ \| '__|
    | |_| | | | | | |  __/ | (_| (_) | | | \ V /  __/ |  | || (_) | |   
     \__|_|_| |_| |_|\___|  \___\___/|_| |_|\_/ \___|_|   \__\___/|_|   


    """
    # Display banner
    print(Fore.YELLOW + Style.BRIGHT + banner)

    # Prompt for number of minutes with a colorful input message
    print(Fore.CYAN + "Enter a number of minutes:", end=" ")
    minutes = int(input())

    # Calculate years, days, and hours
    years, days = divmod(minutes, 60 * 24 * 365)
    days = divmod(days, 24)[0]

    # Display results with colorful output messages
    print(Fore.GREEN + f"\n{minutes} minutes is approximately {years} years, {days} days")
    input("\nPress Enter to Re-run ...")           
