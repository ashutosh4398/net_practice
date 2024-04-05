"""
a1 = [[1,2,3],[2,3],[4,5,1],[1,5,6],[2,1,4,5,6],[88],[1,2,4,5,4],[44]]
-> addition of individual subarrays
transform, reduce subarrays


-> combine only consecutives
-> sum of digits of new should be less than equal to 24
[1,2,3,2,3]
"""

def main():
    a1 = [[1,2,3],[2,3],[4,5,1],[1,5,6],[2,1,4,5,6],[1],[1,2,4,5,4],[1]]
    
    # a1 = [[1, 2, 3, 2, 3, 4, 5, 1],[1,5,6],[2,1,4,5,6],[88],[1,2,4,5,4],[44]]
    # a1 = [[1,2,3],[2,3],[4,5,1],[1,5,6],[2,1,4,5,6],[88],[1,2,4,5,4],[44]]
    final = [a1[0]]
    for i,sub in enumerate(a1[1:],start=1):
        prev = final[-1]
        if sum(prev + a1[i]) <= 24:
            final[-1] = prev + a1[i]
            continue
        final.append(a1[i])
        
    print(final)


"""
obj1 = [
{'title': 1, 'id':[5,4,7]},
{'title': 2, 'id':[1,3,7]},
{'title': 3, 'id':[88,34,1]},
{'title': 4, 'id':[2,11,22]},
]

# obj => idx+1 => refer
obj2 = [{idx:idx+1} for idx in range(100)]

newly mapped ids
filter obj2, -> only show used references
-> 
"""
# def main():
#     obj1 = [
#         {'title': 1, 'id':[5,4,7]},
#         {'title': 2, 'id':[1,3,7]},
#         {'title': 3, 'id':[88,34,1]},
#         {'title': 4, 'id':[2,11,22]},
#     ]
#     obj2 = [{"id":idx+1} for idx in range(100)]

#     counter = 1
#     ranks= {}
#     for obj in obj1:
#         ids = obj["id"]
#         for (idx, _id) in enumerate(ids):
#             if _id not in ranks:
#                 ranks[_id] = counter
#                 counter += 1
#             ids[idx] = ranks[_id]

#     _obj2 = [None for _ in ranks]
#     for k,v in ranks.items():
#         indx = v
#         _obj2[indx-1] = obj2[k-1]

#     print(_obj2)

    


if __name__ == "__main__":
    main()