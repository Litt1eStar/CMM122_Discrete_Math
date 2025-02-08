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
            set_union(sets[0], sets[1])
        elif choice == 2:
            set_intersection(sets[0], sets[1])
        elif choice == 3:
            set_difference(sets[0], sets[1])
        elif choice == 4:
            set_complement()

def set_union(setA: list, setB: list):        
    #Merge 2 set together
    for val in setB:
        setA.append(val)
        
    #Then Sorting it using Bubble Sort Algorithm
    listA = list(setA)
    for i in range(len(listA)):
        for j in range(len(listA) - i - 1):
            if(listA[j] > listA[j+1]):
                listA[j], listA[j+1] = listA[j+1], listA[j]
    
    print(listA)
            

def set_intersection(setA: list, setB: list):
    result_set = []

    for val in setA:
        for lookupVal in setB:
            if(lookupVal == val and not result_set.__contains__(lookupVal)):
                result_set.append(lookupVal)
                break
    
    print(f"Set A : {setA} | Set B : {setB} \nSet A Intersect with Set B = {result_set}")

def set_difference(setA: list, setB: list):
    result_set = []
    for val in setA:
        for lookupVal in setB:
            if(val == lookupVal):
                break
            elif(val != lookupVal and not result_set.__contains__(val)):
                result_set.append(val)
        

    print(f"Set A : {setA} | Set B : {setB} \nSet A Difference with Set B = {result_set}")

def set_complement():
    print("Performing Set Complement...")

def create_set():
    sizeA = int(input("Size of Set A: "))
    sizeB = int(input("Size of Set B: "))
    
    setA = []
    setB = []
    
    for i in range(sizeA):
        val = int(input(f"Element {i} | Value : "))
        setA.append(val)
        
    for i in range(sizeB):
        val = int(input(f"Element {i} | Value : "))
        setB.append(val)
        
    return [setA, setB]