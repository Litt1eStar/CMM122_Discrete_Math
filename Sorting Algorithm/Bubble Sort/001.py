numbers = [4,5,1,3,2, 9,0 ,2, 1,3 ,12, 40 ,23, 4,5 , 0, 90]

def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)):
        swapped = False
        for j in range(0, len(list_of_numbers) - i - 1):
            if(list_of_numbers[j] > list_of_numbers[j + 1]):
                list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]
                swapped = True
        if not swapped:
            break
        
           
def print_array(array):
    for i in range(len(array)):
        print(array[i])

bubble_sort(numbers)
print_array(numbers)
                