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

        if choice == 1:
            set_union()
        elif choice == 2:
            set_intersection()
        elif choice == 3:
            set_difference()
        elif choice == 4:
            set_complement()

def set_union():
    print("Performing Set Union...")

def set_intersection():
    print("Performing Set Intersection...")

def set_difference():
    print("Performing Set Difference...")

def set_complement():
    print("Performing Set Complement...")
