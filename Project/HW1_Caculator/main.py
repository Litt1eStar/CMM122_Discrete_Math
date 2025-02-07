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
    
    if(choice == 1):main_matrix()
    elif(choice == 2):main_function_and_relation()
    elif(choice == 3):main_set()
    elif(choice == 4):main_menu()
    
def main_matrix():
    print("Choose Operation")
    print("(1) Addition")
    print("(2) Subtraction")
    print("(3) Multiply")
    print("(4) Go Previous Page")
    
    choice = int(input(":"))
    print(choice)

def main_function_and_relation():
    print("Choose Operation")
    print("(1) Check Function")
    print("(2) Go Previous Page")
    return

def main_set():
    print("Choose Operation")
    print("(1) Union")
    print("(2) Intersect")
    print("(3) Difference")
    print("(4) Complement")
    print("(5) Go Previous Page")
    return

main()