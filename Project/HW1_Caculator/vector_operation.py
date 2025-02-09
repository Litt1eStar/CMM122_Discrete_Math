from utils import get_choice


def vector_menu():
    while True:
        print("\nVector Operations:")
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
    
    if(len(vector_a) != len(vector_b)):
        print("Vector have to be same size")
        return
    
    result_vector = []
    for i in range(len(vector_a)):result_vector.append(vector_a[i] + vector_b[i])
    print(f"Result Vector: {result_vector}")
        
    
def vector_subtraction():
    vectors = create_two_vector()
    vector_a = vectors[0]
    vector_b = vectors[1]
    
    if(len(vector_a) != len(vector_b)):
        print("Vector have to be same size")
        return
    
    result_vector = []
    for i in range(len(vector_a)):result_vector.append(vector_a[i] - vector_b[i])
    print(f"Result Vector: {result_vector}")

def vector_scalar_multiplication():
    vector_a = create_single_vector()
    scalar_value = int(input("Scalar Value for Multiply to Vector: "))
    
    for i in range(len(vector_a)):vector_a[i] *= scalar_value
    print(f"Result Vector: {vector_a}")
    
def vector_dot_product():
    vectors = create_two_vector()
    vector_a = vectors[0]
    vector_b = vectors[1]

    if(len(vector_a) != len(vector_b)):
        print("Vector have to be same size")
        return

    result = 0
    for i in range(len(vector_a)):result+=vector_a[i]*vector_b[i]
    
    print(f"Vector A: {vector_a}, Vector B: {vector_b} | Dot Product = {result}")
    
def vector_cross_product():
    return

def vector_magnitude():
    return

def vector_normalization():
    return

def create_two_vector():
    size_of_vector = int(input("Size of Vector(2, 3): "))

    if size_of_vector not in [2,3]:
        print("This program support only 2D and 3D Matrix")
        return
    
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
        
def create_single_vector():
    size_of_vector = int(input("Size of Vector(2, 3): "))
    
    if size_of_vector not in [2,3]:
        print("This program support only 2D and 3D Matrix")
        return
    
    vector_a = []
    
    for i in range(size_of_vector):
        vector_index = 'i' if i == 0 else 'j' if i == 1 else 'k' if i == 2 else None
        val = int(input(f"First Vector | {vector_index}: "))
        vector_a.append(val)
        
    return vector_a