from pprint import pprint
from typing import List

MATRIX = List[List[int]]

def transposeMatrix(matrix: MATRIX) -> MATRIX:
    # initial transpose matrix
    row, col = len(matrix), len(matrix[0]) 
    transpose: MATRIX = [[None for _ in range(row)] for _ in range(col)]
    
    for i in range(row):
        for j in range(col):
            transpose[j][i] = matrix[i][j]
    return transpose

ex1 = [
    [1,2]
]

pprint(transposeMatrix(ex1))

