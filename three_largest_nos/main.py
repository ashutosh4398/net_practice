def insert(arr, element, pos):
    for i in range(pos):
        arr[i] = arr[i+1]
    arr[pos] = element

def findThreeLargestNumbers(array, n=3):
    # Write your code here.
    largest_nos = [None for _ in range(n)]
    for elem in array:
        for i in range(n-1,-1,-1):
            if not largest_nos[i]:
                largest_nos[i] = elem
                break
            if largest_nos[i] < elem:
                insert(largest_nos, elem, i)
                break
    
    return largest_nos

x = findThreeLargestNumbers([10,5,9,10,12]);
print(x)