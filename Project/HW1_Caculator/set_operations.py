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