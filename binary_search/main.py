def binarySearch(array, target, start=0,end=None):
    if end is None:
        end = len(array) - 1
    
    mid = (start + end)//2
    if (array[mid] == target):
        return mid
    elif (start == end):
        return -1;
    elif (target < array[mid]):
        return binarySearch(array, target, start, mid-1)
    return binarySearch(array, target, mid+1, end)


    