numbers = [4,2,5,6,7,9,3]

def linear_seach(array, target_number):
    i = 0
    location = -1
    while(i <= len(array) and numbers[i]!=target_number):
        i+=1

    if(i<=len(array)):
        location = i
    
    return location    

print(linear_seach(numbers, 5))