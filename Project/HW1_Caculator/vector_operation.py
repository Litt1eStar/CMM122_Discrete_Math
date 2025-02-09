from utils import get_choice


def vector_menu():
    while True:
        print("\nVector Operations:")
        print("(1) Addition")
        print("(2) Subtraction")
        print("(3) Scalar Multiplication")
        print("(4) Dot Product")
        print("(5) Cross Product")
        print("(6) Return to Mainmenu")

        choice = get_choice(1, 6)
        if choice == 6:
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
            
def vector_addition(vectors = None):
    if(vectors == None):
        vectors = create_two_vector()
    
    vector_a = vectors[0]
    vector_b = vectors[1]
    
    if(len(vector_a) != len(vector_b)):
        print("Vector have to be same size")
        return
    
    result_vector = []
    for i in range(len(vector_a)):result_vector.append(vector_a[i] + vector_b[i])
    print(f"Result Vector: {result_vector}")
    return result_vector
    
def vector_subtraction(vectors = None):
    if(vectors == None):
        vectors = create_two_vector()
    
    vector_a = vectors[0]
    vector_b = vectors[1]
    
    if(len(vector_a) != len(vector_b)):
        print("Vector have to be same size")
        return
    
    result_vector = []
    for i in range(len(vector_a)):result_vector.append(vector_a[i] - vector_b[i])
    print(f"Result Vector: {result_vector}")
    return result_vector

def vector_scalar_multiplication(vector_a = None, scalar_value = None):
    if(vector_a == None):
        vector_a = create_single_vector()
    
    if(scalar_value == None):
        scalar_value = int(input("Scalar Value for Multiply to Vector: "))
    
    for i in range(len(vector_a)):vector_a[i] *= scalar_value
    print(f"Result Vector: {vector_a}")
    return vector_a
    
def vector_dot_product(vectors = None):
    if(vectors==None):
        vectors = create_two_vector()
    
    vector_a = vectors[0]
    vector_b = vectors[1]

    if(len(vector_a) != len(vector_b)):
        print("Vector have to be same size")
        return

    result = 0
    for i in range(len(vector_a)):result+=vector_a[i]*vector_b[i]
    
    print(f"Vector A: {vector_a}, Vector B: {vector_b} | Dot Product = {result}")
    return result

def vector_cross_product(vectors = None):
    if(vectors == None):
        vectors = create_two_vector()
    
    vector_a = vectors[0]
    vector_b = vectors[1]

    if len(vector_a) != 3 or len(vector_b) != 3:
        print("Cross product is only defined for 3-dimensional vectors")
        return

    result_vector = [
        vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1],  
        vector_a[2] * vector_b[0] - vector_a[0] * vector_b[2],  
        vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]   
    ]
    
    print(f"Cross Product: {result_vector}")
    
    return result_vector

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