def productSum(array, depth=1):
    # array can either contain interger or subarrays
    depth_sum = 0

    if isinstance(array, list) and not array:
        return 1*depth

    for elem in array:
        if isinstance(elem, list):
            product = productSum(elem, depth=depth+1)
            depth_sum += product
        else:
            depth_sum += elem

    return depth_sum * depth


# arr = [[[]]] # 4
arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

print(productSum(arr))