numbers = [4,2,5,6,7,9,3]

def linear_search(list_of_numbers, target_number):
    location = -1
    for i in range(len(list_of_numbers)):
        if(list_of_numbers[i]==target_number):
            location = i
    return location

print(linear_search(numbers, 4))