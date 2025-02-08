from utils import get_choice

def set_menu():
    while True:
        print("\nSet Operations:")
        print("(1) Union")
        print("(2) Intersect")
        print("(3) Difference")
        print("(4) Complement")
        print("(5) Return to Previous Menu")

        choice = get_choice(1, 5)
        if choice == 5:
            break
        
        sets = create_set()
        if choice == 1:
            set_union()
        elif choice == 2:
            set_intersection(sets[0], sets[1])
        elif choice == 3:
            set_difference()
        elif choice == 4:
            set_complement()

def set_union():
    print("Performing Set Union...")

def set_intersection(setA, setB):
    result_set = {*{}}
    
    for val in setA:
        for lookupVal in setB:
            if(lookupVal == val and not result_set.__contains__(lookupVal)):
                result_set.add(lookupVal)
                break
    
    print(f"Set A : {setA} | Set B : {setB} \nSet A Intersect with Set B = {result_set}")

def set_difference():
    print("Performing Set Difference...")

def set_complement():
    print("Performing Set Complement...")

def create_set():
    sizeA = int(input("Size of Set A: "))
    sizeB = int(input("Size of Set B: "))
    
    setA = {*{}}
    setB = {*{}}
    
    for i in range(sizeA):
        val = int(input(f"Element {i} | Value : "))
        setA.add(val)
        
    for i in range(sizeB):
        val = int(input(f"Element {i} | Value : "))
        setB.add(val)
        
    return [setA, setB]