"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a 
given number of rows like this: (you may want to display this pattern 
in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
"""


import typing
import math
from pprint import pprint

class Solution:
    @staticmethod
    def convert(s: str, numRows: int) -> str:

        singleBlockLength = numRows + (numRows - 2)
        numBlocks = math.ceil(len(s)/singleBlockLength)
        numCols = numBlocks * (1+numRows-2)
        
        matrix = [["_" for __ in range(numCols)] for _ in range(numRows)]
        
        matrix_idx = 0
        for i in range(numRows):
            for j in range(numCols):
                matrix[i][j] = 



Solution.convert("PAYPALISHIRING", 3)
        
        
