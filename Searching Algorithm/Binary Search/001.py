import math

numbers = [1,2,3,4,5,6,7,8,9]

def binary_search(array, target_number):
    i = 0
    j = len(array)
    location = -1
    while(i < j):
        m = math.floor((i+j)/2)
        if(target_number > array[m]):i = m + 1
        else: j = m
    
    if(array[i] == target_number):
        location = i
    
    return location

print(binary_search(numbers, 5))            