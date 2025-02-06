import math

numbers = [1,2,3,4,5,6,7,8,9]

def binary_search(list_of_numbers, target_number):
    i = 0
    j = len(list_of_numbers)
    location = -1
    while(i < j):
        m = math.floor((i+j)/2)
        if(target_number > list_of_numbers[m]):i = m + 1
        else: j = m
    
    if(list_of_numbers[i] == target_number):
        location = i
    
    return location

print(binary_search(numbers, 5))            