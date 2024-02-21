import random
from typing import List


def merge(array: List[int], left: int, mid: int, right: int) -> None:
    L: List[int] = array[left:mid+1]
    R: List[int] = array[mid+1: right + 1]
    k = left
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        array[k] = R[j]
        j += 1
        k += 1

def merge_sort(array: List[int], left: int, right: int) -> None:
    if left < right:
        mid = (left + right)//2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)

def main():
    # array: List[int] = [10,6,20,7,5,9]
    array: List[int] = [random.randint(1,20) for _ in range(20)]
    print(array)
    merge_sort(array, 0, len(array)-1)
    print(array)

if __name__ == "__main__":
    main()