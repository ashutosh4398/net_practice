"""
array_1 = [[1,1,2,3], [2,2,3,4], [3,5,6,7], [9,11,12,13]]
array_2 = [[1,3], [3,4], [5,6], [9,10], [12,13]]
8:03
find all number in array_1 which are not present in array_2. 
ignore all numbers of array_1 which occur in more than 1 sub arrays.
"""

def flatten(arr):
    return [i for sub_arr in arr for i in sub_arr]

def main():
    array_1 = [[1,1,2,3], [2,2,3,4], [3,5,6,7], [9,11,12,13]]
    array_2 = [[1,3], [3,4], [5,6], [9,10], [12,13]]
    
    flattened_arr_1 = flatten(array_1)
    flattened_arr_2 = flatten(array_2)

    resultants = list(set(flattened_arr_1) - set(flattened_arr_2))
    counter = {}
    
    for i in resultants:
        for idx, sub_arr in enumerate(array_1):
            if i in sub_arr:
                counter[i] = counter.get(i, 0) + 1
                continue
    
    return [num for num,count in counter.items() if count == 1]

print(main()) # [11, 7]