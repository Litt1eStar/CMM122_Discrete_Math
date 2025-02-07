def main():
    isExit = False
    
    main_menu()
    
    if(choice == '2'): exit()
    else: operator_ui()
        
            
def main_menu():
    global choice
    print("Welcome to Super Caculator")
    print("(1) Start")
    print("(2) Exit")
    
    choice = int(input(": "))
    if(choice == '2'): exit()
    else: operator_ui()
        
def operator_ui():
    print("What do you want to do?")
    print("(1) Matrix")
    print("(2) Function and Relation")
    print("(3) Set")
    print("(4) Return to Main Menu")
    
    choice = int(input(":"))
    
    if(choice == 1):matrix()
    elif(choice == 2):function_and_relation()
    elif(choice == 3):Set()
    elif(choice == 4):main_menu()
def matrix():
    print("Matrix")
    return

def function_and_relation():
    print("Function and Relation")
    return

def Set():
    print("Set")
    return

main()