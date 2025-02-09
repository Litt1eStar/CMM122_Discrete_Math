from utils import get_choice


def vector_menu():
    while True:
        print("\Vector Operations:")
        print("(1) Addition")
        print("(2) Subtraction")
        print("(3) Scalar Multiplication")
        print("(4) Dot Product")
        print("(5) Cross Product")
        print("(6) Find Vector Magnitude")
        print("(7) Vector Normalizatino")
        print("(8) Return to Mainmenu")

        choice = get_choice(1, 8)
        if choice == 8:
            break
        
        if choice == 1:
            vector_addition()
        elif choice == 2:
            vector_subtraction()
        elif choice == 3:
            vector_scalar_multiplication()
        elif choice == 4:
            vector_dot_product()
        elif choice == 5:
            vector_cross_product()
        elif choice == 6:
            vector_magnitude()
        elif choice == 7:
            vector_normalization()
            
def vector_addition():
    return

def vector_subtraction():
    return

def vector_scalar_multiplication():
    return

def vector_dot_product():
    return

def vector_cross_product():
    return

def vector_magnitude():
    return

def vector_normalization():
    return