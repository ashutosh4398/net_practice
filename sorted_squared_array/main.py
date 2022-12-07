from typing import List

def sortedSquaredArray(array: List[int]) -> List[int]:
    array_length: int = len(array)
    min_index: int = 0
    max_index: int = array_length - 1
    output_array: List[int] = [0 for _ in range(array_length)]
    while array_length > 0:
        min_index_elem, max_index_elem = array[min_index], array[max_index]
        if abs(min_index_elem) >= abs(max_index_elem):
            min_index += 1
            output_array[array_length - 1] = min_index_elem**2
        if abs(min_index_elem) < abs(max_index_elem):
            max_index -= 1
            output_array[array_length - 1] = max_index_elem**2
        array_length -= 1
    return output_array
