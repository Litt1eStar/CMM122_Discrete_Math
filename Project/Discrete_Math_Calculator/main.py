from utils import get_choice, clear_screen
from matrix_operations import matrix_menu
from function_relation import function_menu
from set_operations import set_menu
from vector_operation import vector_menu
from base_number_system_operation import base_number_system_menu

from colorama import Fore, Style
from tabulate import tabulate

def main():
    while True:
        choice = main_menu()
        
        if(choice == '2'): exit()
        else: operator_ui()
            
            
def main_menu():
    clear_screen()
    menu_options = [
            ["1", "Start"],
            ["2", "Exit"],
        ]

    print(Fore.RED + Style.BRIGHT + "\nWelcome to Super Calculator\n" + Style.RESET_ALL)
    print(tabulate(menu_options, headers=["Option", "Operation"], tablefmt="mixed_outline"))
    
    choice = get_choice(1, 2)
    return choice
        
def operator_ui():
    while True:
        clear_screen()
        menu_options = [
            ["1", "Matrix"],
            ["2", "Function and Relation"],
            ["3", "Set"],
            ["4", "Vector"],
            ["5", "Base Number System"],
            ["6","Return to Main Menu"]
        ]

        print(Fore.GREEN+ Style.BRIGHT + "\n     What do you want to do?\n" + Style.RESET_ALL)
        print(tabulate(menu_options, headers=["Option", "Operation"], tablefmt="mixed_outline"))
        
        choice = get_choice(1, 6)
        
        if(choice == 1):matrix_menu()
        elif(choice == 2):function_menu()
        elif(choice == 3):set_menu()
        elif(choice == 4):vector_menu()
        elif(choice == 5):base_number_system_menu()
        elif(choice == 6):break

main()