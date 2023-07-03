def swap(array, pos):
    array[pos], array[pos+1] = array[pos+1], array[pos]

def bubbleSort(array):
    # Write your code here.
    num_of_iterations = len(array)
    for j in range(num_of_iterations):
        is_swapped = False
        for i in range(len(array)-1-j):
            if(array[i] > array[i+1]):
                swap(array, i)
                is_swapped = True
        if is_swapped == False:
            break
    return array

print(bubbleSort([8,5,2,9,5,6,3]))
