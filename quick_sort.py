import random
from typing import List

def partition_array(array: List[int], left: int, right: int) -> int:
    """
        returns partition index
    """
    l,r = left, right
    pivot_idx = r
    while l < r:
        while array[l] < array[pivot_idx]:
            l += 1
        while array[r] >= array[pivot_idx]:
            r -= 1
        if l < r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1
    array[pivot_idx], array[l] = array[l], array[pivot_idx]
    return l
        

def quick_sort(array: List[int], left: int, right: int) -> None:
    """
        Sorts the array in-place
    """
    if left < right:
        partition = partition_array(array, left, right)
        quick_sort(array, left, partition-1)
        quick_sort(array, partition + 1, right)


def main()-> None:
    # array: List[int] = [10, 6, 20, 7, 5, 9]
    array: List[int] = [random.randint(1,20) for _ in range(20)]
    print(array)
    quick_sort(array, 0, len(array)-1)
    print(array)

if __name__ == "__main__":
    main()