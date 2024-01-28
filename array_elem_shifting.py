# TODO: naive approach :-
# l = [1,2,3,4,5]
# N = len(l)
# key = 1

# for i in range(key):
#     l.append(l[i])

# N_updated = len(l)
# for i in range(len(l)):
#     l[i] = l[(i+key)%N_updated]

# print(l[:N])

# TODO: PRO APPROACH
def reverse_array(seq, l, r):
    """
    reverses sequence only between given indices
    """
    while l < r:
        seq[l], seq[r] = seq[r], seq[l]
        l, r = l+1, r-1
    return seq

def transform(array, key):
    n = len(array)
    key = key % n
    reversed_input = reverse_array(array, 0, n-1)
    reversed_input = reverse_array(reversed_input, 0, key-1)
    reversed_input = reverse_array(reversed_input, key, n-1)
    return reversed_input


