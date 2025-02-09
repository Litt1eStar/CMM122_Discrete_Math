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
    vectors = create_two_vector()
    vector_a = vectors[0]
    vector_b = vectors[1]
    result_vector = [vector_a[0]+vector_b[0], vector_a[1]+vector_b[1], vector_a[2]+vector_b[2]]
    print(result_vector)
    
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

def create_two_vector():
    size_of_vector = 3

    vector_a = []
    vector_b = []
    for i in range(size_of_vector):
        vector_index = 'i' if i == 0 else 'j' if i == 1 else 'k' if i == 2 else None
        val = int(input(f"First Vector | {vector_index}: "))
        vector_a.append(val)
        
    for i in range(size_of_vector):
        vector_index = 'i' if i == 0 else 'j' if i == 1 else 'k' if i == 2 else None
        val = int(input(f"Second Vector | {vector_index}: "))
        vector_b.append(val)
    
    return [vector_a, vector_b]
        