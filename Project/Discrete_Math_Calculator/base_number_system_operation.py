from utils import get_choice, clear_screen
from colorama import Fore, Style
from tabulate import tabulate

def base_number_system_menu():
    while True:
        clear_screen()
        menu_options = [
            ["1", "Addition"],
            ["2", "Subtraction"],
            ["3", "Multiplication"],
            ["4", "Scalar Multiplication"],
            ["5", "Transpose"],
            ["6", "Determinant"],
            ["7", "Inverse"],
            ["8", "Return to Previous Menu"]
        ]

        print(Fore.GREEN + "\n\Base Number System Operation\n" + Style.RESET_ALL)
        print(tabulate(menu_options, headers=["Option", "Operation"], tablefmt="fancy_grid"))


        choice = get_choice(1, 8)
        if choice == 8:
            break
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)