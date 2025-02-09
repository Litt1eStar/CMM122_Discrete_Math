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
