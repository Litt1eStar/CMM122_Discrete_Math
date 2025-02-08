def get_choice(min_val, max_val):
    while True:
        try:
            choice = int(input(": "))
            if min_val <= choice <= max_val:
                return choice
            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid Input")
            
def print_matrix(matrix):
    for m in range(len(matrix)):
        for j in range(len(matrix[m])):
            print(matrix[m][j], end=" ")
        print()
