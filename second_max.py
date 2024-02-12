
def find_second_max(arr):
    max_num, second_max = 0, 0
    for i in arr:        
        if i > max_num:
            second_max = max_num
            max_num = i
        if i > second_max and i != max_num:
            second_max = i
    
    return second_max

arr = [10, 20, 19, 21, 55, 3, 2, 51, 55, 55, 54, 55]
print(find_second_max(arr))