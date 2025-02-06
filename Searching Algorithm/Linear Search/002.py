numbers = [4,2,5,6,7,9,3]

def linear_search(array, target_number):
    location = -1
    for i in range(len(array)):
        if(array[i]==target_number):
            location = i
    return location

print(linear_search(numbers, 4))