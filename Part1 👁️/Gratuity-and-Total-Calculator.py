import os

while True:
    os.system("cls")
    # Displaying Banner
    print("\033[1;34m========== Gratuities Calculator ==========\033[0m")

    # Prompting user for input and calculating gratuity and total in a single line
    subtotal, gratuity_rate = map(float, input("\n\033[1;32mEnter the subtotal and gratuity rate (%) [Sperate with space] >>> \033[0m").split())

    # Calculating Gratuity and Total in a single line using formulae
    gratuity, total = subtotal * (gratuity_rate / 100), subtotal * (1 + gratuity_rate / 100)

    # Displaying the calculated Gratuity and Total
    print(f"\033[1mGratuity:\033[0m \033[1;33m{gratuity:.2f}\033[0m")
    print(f"\033[1mTotal:\033[0m \033[1;32m{total:.2f}\033[0m")
    input("\nPress Enter to re-run the Calculator ...")

