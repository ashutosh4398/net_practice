import random

def find_second_max(arr):
    max_num, second_max = 0, 0
    for i in arr:        
        if i > max_num:
            second_max = max_num
            max_num = i
        if i > second_max and i != max_num:
            second_max = i
    
    return second_max

arr = [random.randint(1, 101) for _ in range(10)]
print(arr)
print(find_second_max(arr))