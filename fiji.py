def find_first_and_second_max(array):
    if len(array) < 2:
        return (-1, -1)
    # initial indices of first and second max
    first_max = 0 if array[0] > array[1] else 1
    second_max = 0 if array[0] < array[1] else 1
    
    for idx in range(2, len(array)):
        if array[idx] > array[first_max]:
            second_max = first_max
            first_max = idx
        elif array[idx] > array[second_max]:
            second_max = idx

    return first_max, second_max

def find_respective_greenest_gardens(gardens):
    greenest_garden_idx, second_greenest_idx = find_first_and_second_max(gardens)
    if greenest_garden_idx == -1:
        return garden
    greenest_garden = gardens[greenest_garden_idx]
    second_greenest = gardens[second_greenest_idx]

    for idx, garden in enumerate(gardens):
        if garden == greenest_garden:
            gardens[idx] = second_greenest
            continue
        gardens[idx] = greenest_garden

    return gardens


    
def main(lines):  
    # number of gardens
    n = int(lines[0])
    gardens = [int(x) for x in lines[1].split()]
    find_respective_greenest_gardens(gardens)
    print(gardens)
    
if __name__ == '__main__':
    lines = ['2', '10 8 -7 9 11 10 4 -7 -7 3']

    # for l in sys.stdin:
    #     lines.append(l.rstrip('\r\n'))
    main(lines)
