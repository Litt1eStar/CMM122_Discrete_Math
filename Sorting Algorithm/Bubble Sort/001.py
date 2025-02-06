numbers = [4,5,1,3,2, 9,0 ,2, 1,3 ,12, 40 ,23, 4,5 , 0, 90]

def bubble_sort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):
            if(array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
        
           
def print_array(array):
    for i in range(len(array)):
        print(array[i])

bubble_sort(numbers)
print_array(numbers)
                