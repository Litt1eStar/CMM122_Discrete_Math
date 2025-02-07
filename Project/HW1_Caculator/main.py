from utils import get_choice
from matrix_operations import matrix_menu
from function_relation import function_menu
from set_operations import set_menu

def main():
    
    while True:
        choice = main_menu()
        
        if(choice == '2'): exit()
        else: operator_ui()
            
            
def main_menu():
    print("Welcome to Super Caculator")
    print("(1) Start")
    print("(2) Exit")
    
    choice = get_choice(1, 2)
    return choice
        
def operator_ui():
    while True:
        print("What do you want to do?")
        print("(1) Matrix")
        print("(2) Function and Relation")
        print("(3) Set")
        print("(4) Return to Main Menu")
        
        choice = get_choice(1, 4)
        
        if(choice == 1):matrix_menu()
        elif(choice == 2):function_menu()
        elif(choice == 3):set_menu()
        elif(choice == 4):break

main()