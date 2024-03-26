"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

Input: n = 3

Output: [
[1,2,3],
[8,9,4],
[7,6,5]
]
"""

from pprint import pprint
from typing import List, Literal


class Solution:
    def create_spiral_matrix(self, n: int) -> List[List[int]]:
        matrix: List[List[Literal[0]]] = [[-1 for _ in range(n)] for _ in range(n)]
        ROW_MIN, ROW_MAX, COL_MIN, COL_MAX = 0, n - 1, 0, n - 1
        row, col = 0, 0
        count = 1
        while count <= n**2:
            while col <= COL_MAX:
                matrix[row][col] = count
                count, col = count + 1, col + 1
            ROW_MIN, row, col, ROW_MAX = ROW_MIN + 1, row + 1, col - 1, ROW_MAX

            while row <= ROW_MAX:
                matrix[row][col] = count
                count, row = count + 1, row + 1
            COL_MIN, row, col, COL_MAX = COL_MIN, row - 1, col - 1, COL_MAX - 1

            while col >= COL_MIN:
                matrix[row][col] = count
                count, col = count + 1, col - 1
            ROW_MIN, row, col, ROW_MAX = ROW_MIN, row - 1, col + 1, ROW_MAX - 1

            while row >= ROW_MIN:
                matrix[row][col] = count
                count, row = count + 1, row - 1
            COL_MIN, row, col, COL_MAX = COL_MIN + 1, row + 1, col + 1, COL_MAX

        return matrix


def main():
    s = Solution()
    pprint(s.create_spiral_matrix(7))


if __name__ == "__main__":
    main()
