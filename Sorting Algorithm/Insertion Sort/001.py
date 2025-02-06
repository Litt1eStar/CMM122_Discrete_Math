numbers = [3,4,2,1,6,7,9,5]

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while(j > 0 and array[j] < array[j - 1]):
            array[j], array[j - 1] = array[j - 1], array[j]
            j-=1
            
def print_array(array):
    for i in range(len(array)):
        print(array[i])
        
insertion_sort(numbers)
print_array(numbers)